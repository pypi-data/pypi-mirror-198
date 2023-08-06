# -*- coding: utf-8 -*-
import asyncio
import re
from typing import List, Union, AsyncIterator
import aiohttp

from .abstract import Vault
from .config import validate_ip, flatten
from .exceptions import (
    CyberarkAPIException, CyberarkException, AiobastionException
)

BASE_FILECATEGORY = ("platformId", "userName", "address", "name")
SECRET_MANAGEMENT_FILECATEGORY = ("automaticManagementEnabled", "manualManagementReason", "lastModifiedTime",
                                  "lastReconciledTime", "lastVerifiedTime", "status")


class PrivilegedAccount:
    """Base class to be used with accounts fonctions"""

    def __init__(self, name: str, platformId: str, safeName: str,
                 platformAccountProperties: dict = None, secret: str = "", secretType: str = None,
                 secretManagement: dict = None,
                 remoteMachinesAccess: dict = None,
                 id: str = "", address: str = "", userName: str = "",
                 **other):
        self.secret = secret
        if remoteMachinesAccess is not None:
            if not all([k in ["remoteMachines", "accessRestrictedToRemoteMachines"]
                        for k in remoteMachinesAccess.keys()]):
                raise AiobastionException("remoteMachinesAccess is not a valid dictionary")
        if secretManagement is None:
            secretManagement = {"automaticManagementEnabled": True, "manualManagementReason": ""}
        self.remoteMachinesAccess = remoteMachinesAccess
        self.secretManagement = secretManagement
        self.secretType = secretType
        if secretType not in [None, "password", "key"]:
            raise AiobastionException("secretType is not valid")
        if platformAccountProperties is None:
            platformAccountProperties = {}
        self.platformAccountProperties = platformAccountProperties
        self.safeName = safeName
        self.platformId = platformId
        self.userName = userName
        self.address = address
        self.name = name
        self.id = id
        for k, v in other.items():
            setattr(self, k, v)

    def get_name(self):
        return f"{self.address}-{self.userName}"

    def to_json(self):
        json_object = {"id": self.id, "name": self.name, "address": self.address, "userName": self.userName,
                       "platformId": self.platformId, "safeName": self.safeName, "secret": self.secret,
                       "platformAccountProperties": self.platformAccountProperties,
                       "secretManagement": self.secretManagement}
        if self.remoteMachinesAccess is not None:
            json_object["remoteMachinesAccess"] = self.remoteMachinesAccess
        if self.secretType is not None:
            json_object["secretType"] = self.secretType

        return json_object

    def __str__(self):
        strrepr = self.to_json()
        return str(strrepr)

    def cpm_status(self):
        if "status" in self.secretManagement:
            # 'success' for 'failure'
            return self.secretManagement["status"]
        elif "automaticManagementEnabled" in self.secretManagement and \
                not self.secretManagement["automaticManagementEnabled"]:
            return "Deactivated"
        else:
            return "No status (yet)"

    def last_modified(self, days=True):
        import time
        if "lastModifiedTime" in self.secretManagement:
            ts = self.secretManagement["lastModifiedTime"]
            if days:
                return int((int(time.time()) - ts) / 86400)
            else:
                return ts


def _filter_account(account: dict, filters: dict):
    """
    This function helps to ensure that search accounts match with requested accounts
    :param account: one json cyberark repr of a privileged address
    :param filters: one dict like username: admin
    :return: check if content of privileged FC is exactly the content of the filter
    """
    for k, v in filters.items():
        if k.lower() == "username":
            if "userName" not in account:
                return False
            if account['userName'].upper() != v.upper():
                return False
        elif k.lower() == "address":
            if account['address'].upper() != v.upper():
                return False
        elif k.lower() in ("platform", "platformid"):
            if account['platformId'].upper() != v.upper():
                return False
        elif k not in account['platformAccountProperties']:
            return False
        elif account['platformAccountProperties'][k] != v:
            return False
    return True


class Account:
    def __init__(self, epv: Vault):
        self.epv = epv

    async def handle_acc_list(self, api_call, account, *args, **kwargs):
        if isinstance(account, list):
            tasks = []
            for a in account:
                if not isinstance(a, PrivilegedAccount) and not re.match('[0-9]*_[0-9*]', a):
                    raise AiobastionException("You must call the function with PrivilegedAccount or list of Privileged "
                                              "Accounts")

                tasks.append(api_call(a, *args, **kwargs))

            return await asyncio.gather(*tasks, return_exceptions=True)
        elif isinstance(account, PrivilegedAccount) or re.match('[0-9]*_[0-9*]', account):
            return await api_call(account, *args, **kwargs)
        else:
            raise AiobastionException("You must call the function with PrivilegedAccount or list of Privileged Accounts"
                                      "(or valid account_id for some functions)")

    async def handle_acc_id_list(self, method, url, accounts, data=None):
        """
        Utility function for handling a list of accounts id in parameter of url
        :param method: http valid method
        :param url: lambda function that return the url with an account_id parameter
        :param accounts: list of address id
        :param data: if relevant, a dict that contains data
        :param return_exception: return exceptions as result, or raise

        :return: the result of the subsequent calls
        :
        """

        async def api_call(acc_id):
            return await self.epv.handle_request(method, url(acc_id), data=data)

        return await self.handle_acc_list(api_call, accounts)

    async def add_account_to_safe(self, account: Union[PrivilegedAccount, List[PrivilegedAccount]]) -> str:
        async def api_call(acc):
            return await self.epv.handle_request("post", 'API/Accounts', data=acc.to_json(),
                                                 filter_func=lambda r: r["id"])

        return await self.handle_acc_list(api_call, account)

    async def get_account(self, account_id) -> Union[PrivilegedAccount, List[PrivilegedAccount]]:
        acc = await self.handle_acc_id_list(
            "get",
            lambda a: f"API/Accounts/{a}",
            account_id
        )

        if isinstance(acc, dict):
            return PrivilegedAccount(**acc)
        else:
            return [PrivilegedAccount(**a) for a in acc]

    async def get_privileged_account_id(self, account: PrivilegedAccount):
        if account.id == "":
            acc = await self.search_account_by(username=account.userName, safe=account.safeName,
                                               keywords=account.address)
            if len(acc) != 1:
                return [a.id for a in acc]
            else:
                return acc[0].id
        else:
            return account.id

    async def get_single_account_id(self, account):
        if type(account) is str:
            if re.match(r'\d+_\d+', account) is not None:
                return account
            else:
                raise AiobastionException("The account_id provided is not correct")
        if isinstance(account, PrivilegedAccount):
            return await self.get_privileged_account_id(account)
        else:
            raise AiobastionException("You must provide a valid PrivilegedAccount to function get_account_id")

    async def get_account_id(self, account: Union[PrivilegedAccount, str, List[PrivilegedAccount], List[str]]):
        if isinstance(account, list):
            tasks = [self.get_single_account_id(a) for a in account]
            return flatten(await asyncio.gather(*tasks, return_exceptions=False))
        else:
            return await self.get_single_account_id(account)

    async def link_reconciliation_account(self, account: Union[PrivilegedAccount, List[PrivilegedAccount]],
                                          reconcile_account: PrivilegedAccount):
        return await self.link_account(account, reconcile_account, 3)

    async def link_logon_account(self, account: Union[PrivilegedAccount, List[PrivilegedAccount]],
                                 logon_account: PrivilegedAccount):
        #TODO check the index of logon account at platform level !
        return await self.link_account(account, logon_account, 2)

    async def link_reconcile_account_by_address(self, acc_username, rec_acc_username, address):
        acc, rec_acc = await asyncio.gather(
            self.search_account_by(username=acc_username, address=address),
            self.search_account_by(username=rec_acc_username, address=address))

        if len(acc) > 1:
            raise CyberarkException("More than one address %s with address %s was found !" %
                                    (acc_username, address))
        if len(acc) == 0:
            raise CyberarkException("The address %s with address %s was not found !" % (acc_username, address))

        if len(rec_acc) > 1:
            raise CyberarkException("More than one reconciliation address %s with address %s was found !" %
                                    (rec_acc_username, address))
        if len(rec_acc) == 0:
            raise CyberarkException("The reconciliation address %s with address %s was not found !" %
                                    (rec_acc_username, address))

        return await self.link_reconciliation_account(acc[0], rec_acc[0])

    async def remove_reconcile_account(self, account: Union[PrivilegedAccount, List[PrivilegedAccount]]):
        return await self.unlink_account(account, 3)

    async def remove_logon_account(self, account: Union[PrivilegedAccount, List[PrivilegedAccount]]):
        return await self.unlink_account(account, 2)

    async def unlink_account(self, account: Union[PrivilegedAccount, List[PrivilegedAccount]],
                             extra_password_index: int):
        if extra_password_index not in [1, 2, 3]:
            raise AiobastionException("ExtraPasswordIndex must be between 1 and 3")

        return await self.handle_acc_id_list(
            "delete",
            lambda a: f"API/Accounts/{a}/LinkAccount/{extra_password_index}",
            await self.get_account_id(account)
        )

    async def link_account(self, account: PrivilegedAccount, link_account: PrivilegedAccount, extra_password_index: int,
                           folder="Root") -> bool:
        """
        :param account: The target address
        :param link_account: The linked address (reconcile or logon address)
        :param extra_password_index: 1 for logon, 3 for reconcile
        :param folder: "Root" by default
        :return: True if success, exception otherwise
        """
        if extra_password_index not in [1, 2, 3]:
            raise AiobastionException("ExtraPasswordIndex must be between 1 and 3")
        account_id = await self.get_account_id(account)
        if self.epv.versiontuple(await self.epv.get_version()) > self.epv.versiontuple("12.1.1"):
            data = {
                "safe": link_account.safeName,
                "extraPasswordIndex": extra_password_index,
                "name": link_account.name,
                "folder": folder
            }
        else:
            data = {
                "safe": link_account.safeName,
                "ExtraPassID": extra_password_index,
                "name": link_account.name,
                "folder": folder
            }

        # async def api_call(acc_id):
        #     return await self.epv.handle_request("post", f"API/Accounts/{acc_id}/LinkAccount", data=data)
        #
        # return await self.handle_acc_list(api_call, account_id)

        return await self.handle_acc_id_list(
            "post",
            lambda a: f"API/Accounts/{a}/LinkAccount",
            account_id,
            data
        )

    async def change_password(self, account: Union[PrivilegedAccount, str], change_group=False):
        data = {
            "ChangeEntireGroup": change_group
        }

        return await self.handle_acc_id_list(
            "post",
            lambda acc_id: f"API/Accounts/{acc_id}/Change",
            await self.get_account_id(account),
            data
        )

    async def reconcile(self, account: Union[PrivilegedAccount, str]):
        return await self.handle_acc_id_list(
            "post",
            lambda a: f"API/Accounts/{a}/Reconcile",
            await self.get_account_id(account)
        )

    async def verify(self, account: Union[PrivilegedAccount, str]):
        return await self.handle_acc_id_list(
            "post",
            lambda a: f"API/Accounts/{a}/Verify",
            await self.get_account_id(account)
        )

    def is_valid_username(self, name: str) -> bool:
        special_chars = "\\/.:*?\"<>|\t\r\n\x1F"
        return not (len(name) > 128 or any(c in special_chars for c in name))

    def is_valid_safename(self, name: str) -> bool:
        special_chars = "\\/.:*?\"<>|\t\r\n\x1F"
        return not (len(name) > 28 or any(c in special_chars for c in name))

    async def search_account_by_ip_addr(self, address: Union[PrivilegedAccount, str]):
        """
        This function search accounts using IPv4 address (or with address attribute of PrivilegedAccount object)
        :param address: A PrivilegedAccount object or IPv4 valid address
        :return: A list of "PrivilegedAccount" objects
        """
        if type(address) is str:
            address = address
        elif isinstance(address, PrivilegedAccount):
            address = address.address
        else:
            raise TypeError("search address function returned : First argument of address is not valid")

        if not validate_ip(address):
            raise TypeError(f"The address of the object was not considered as valid IPv4 address {address}")

        return await self.search_account_by(address=address)

    async def search_account(self, expression: str):
        """
        This function search an address using free text search and return a list a Privileged Account objects
        :param expression: List of keywords to search for in accounts, separated by a space.
        :return: List of PrivilegedAccount objects
        """
        return await self.search_account_by(expression)

    async def search_account_by(self, keywords=None, username=None, address=None, safe=None,
                                platform=None, **kwargs) -> List[PrivilegedAccount]:
        """
        This function allow to search using one or more parameters and return list of address id
        :param keywords: free search
        :param username: username search (field "userName")
        :param address: IP address search (field "address")
        :param safe: search in particular safe
        :param platform: search by platform name (no space) (field "platformId")
        :param kwargs: any searchable key = value
        :return: a list of PrivilegedAccounts
        """

        return [account async for account in
                self.search_account_iterator(keywords, username, address, safe, platform, **kwargs)]

    async def search_account_iterator(self, keywords=None, username=None, address=None, safe=None,
                                      platform=None, **kwargs) -> AsyncIterator[PrivilegedAccount]:
        """
        This function allow to search using one or more parameters and return list of address id
        :param keywords: free search
        :param username: username search (field "userName")
        :param address: IP address search (field "address")
        :param safe: search in particular safe
        :param platform: search by platform name (no space) (field "platformId")
        :param kwargs: any searchable key = value
        :return: an async iterator of PrivilegedAccounts
        """

        filtered_args = {k: v for k, v in locals().items() if v and k not in ["safe", "self", "keywords", "kwargs"]}
        filtered_args.update(kwargs)

        page = 1
        has_next_page = True

        while has_next_page:
            accounts = await self.search_account_paginate(page=page, safe=safe, search=keywords, **filtered_args)
            has_next_page = accounts["has_next_page"]
            page += 1
            for a in accounts["accounts"]:
                yield a

    async def search_account_paginate(self, page: int = 1, size_of_page: int = 1000, safe: str = None,
                                      search: str = None, **kwargs):
        """
        Search accounts in a paginated way
        :param search: free search
        :param page: number of page
        :param size_of_page: size of pages
        :param safe: filter on particular safe
        :param kwargs: whatever file category you want to find
        :return:
        """

        try:
            params = {"search": " ".join(kwargs.values())}
        except TypeError:
            raise AiobastionException(f"You can't search on a list here ({kwargs.values()}), provide a string instead")

        if search is not None:
            params["search"] += f" {search}"

        if safe is not None:
            params["filter"] = "safeName eq " + safe

        params["limit"] = size_of_page
        params["offset"] = (page - 1) * size_of_page
        search_results = await self.epv.handle_request("get", "API/Accounts", params=params,
                                                       filter_func=lambda x: x)
        account_list = search_results['value']
        # check for each address if the content of FC match the search
        filtered_account_list = filter(lambda f: _filter_account(f, kwargs), account_list)
        # for each filtered address, build the PrivilegedAccount
        filtered_acc_list = [PrivilegedAccount(**acc) for acc in filtered_account_list]

        has_next_page = "nextLink" in search_results
        return {
            "accounts": filtered_acc_list,
            "has_next_page": has_next_page
        }

    async def connect_using_PSM(self, account, connection_component):
        account_id = await self.get_account_id(account)
        url, head = self.epv.get_url(f"API/Accounts/{account_id}/PSMConnect")
        head["Accept"] = 'RDP'
        body = {"ConnectionComponent": connection_component}

        async with aiohttp.ClientSession(headers=head) as session:
            async with session.post(url, json=body, **self.epv.request_params) as req:
                if req.status != 200:
                    content = await req.json()
                    raise CyberarkAPIException(req.status, content["ErrorCode"], content["ErrorMessage"])

                return await req.read()

    async def disable_password_management(self, account: Union[PrivilegedAccount, List[PrivilegedAccount]],
                                          reason: str = ""):
        data = [
            {"op": "replace", "path": "/secretManagement/automaticManagementEnabled", "value": False},
            {"op": "add", "path": "/secretManagement/manualManagementReason", "value": reason}
        ]

        return await self.handle_acc_id_list(
            "patch",
            lambda account_id: f"API/Accounts/{account_id}",
            await self.get_account_id(account),
            data
        )

    async def resume_password_management(self, account: Union[PrivilegedAccount, List[PrivilegedAccount]]):
        """
        Resume secret management
        :param account: Privileged Account, or address ID
        :return: Updated address
        """
        # account_id = await self.get_account_id(address)

        data = [
            {"op": "replace", "path": "/secretManagement/automaticManagementEnabled", "value": True},
        ]
        return await self.handle_acc_id_list(
            "patch",
            lambda account_id: f"API/Accounts/{account_id}",
            await self.get_account_id(account),
            data
        )
        # return await self.epv.handle_request("patch", f"API/Accounts/{account_id}", data=data)

    async def update_using_list(self, account, data):
        """
        :param account: address, list of accounts, account_id, list of accounts id
        :param data: example :
            data = [
                {"path": "/name", "op": "replace", "value": new_name},
                {"path": "/address", "op": "replace", "value": new_address},
                {"path": "/platformId", "op": "replace", "value": new_platformId},
            ]
        :return: json repr of the address
        """
        return await self.handle_acc_id_list(
            "patch",
            lambda account_id: f"API/Accounts/{account_id}",
            await self.get_account_id(account),
            data
        )

        # return await self.epv.handle_request("patch", 'API/Accounts/' + account_id, data=data)
    # Doc + Test
    def detect_fc_path(self, fc):
        if fc in BASE_FILECATEGORY:
            return "/"
        elif fc in SECRET_MANAGEMENT_FILECATEGORY:
            return "/secretmanagement/"
        else:
            return "/platformaccountproperties/"

    async def update_single_fc(self,  account, file_category, new_value, operation="replace"):

        # if we "add" and FC exists it will replace it
        data = [{"path": f"{self.detect_fc_path(file_category)}{file_category}", "op": operation, "value": new_value}]
        try:
            return await self.update_using_list(account, data)
        except CyberarkAPIException as err:
            if err.err_code == "PASWS164E" and operation == "replace":
                # Try to add FC instead of replacing it
                return await self.update_single_fc(account, file_category, new_value, "add")
            else:
                raise

    async def update_file_category(self, account, file_category, new_value):
        """
        Update the file category (or list of FC) with the new value (or list of new values)
        If the FC does not exist, it will create it

        :param account: address, list of accounts, account_id, list of accounts id
        :param file_category: a file category or a list of file category
        :param new_value: the new value of the list of new values

        """
        data = []
        if isinstance(file_category, list):
            try:
                assert isinstance(new_value, list)
            except AssertionError:
                raise AiobastionException("If file_category is a list, then new value must be a list aswell")
            try:
                assert len(file_category) == len(new_value)
            except AssertionError:
                raise AiobastionException("You must provide the same list size for file_category and values")
            for f,n in zip(file_category, new_value):
                # we trust user and don't check if FC is defined at platform level
                data.append({"path": f"{self.detect_fc_path(f)}{f}", "op": "add", "value": n})
        else:
            data.append({"path": f"{self.detect_fc_path(file_category)}{file_category}", "op": "add", "value": new_value})

        return self.update_using_list(account, data)


    # Doc + Test
    async def restore_last_cpm_version(self, account: PrivilegedAccount, cpm):
        versions = await self.get_secret_versions(account)
        cpm_versions = [v["versionID"] for v in versions if v["modifiedBy"] == cpm]
        if len(cpm_versions) > 0:
            good_ver = max(cpm_versions)
            password_to_set = await self.get_password_version(account,good_ver)
            return await self.set_password(account,password_to_set)
        else:
            raise AiobastionException("There is no CPM version for this account")

    async def restore_last_cpm_version_by_cpm(self, account: PrivilegedAccount, cpm):
        versions = await self.get_secret_versions(account)
        print(versions)
        cpm_versions = [v["versionID"] for v in versions if v["modifiedBy"] == cpm]
        if len(cpm_versions) > 0:
            good_ver = max(cpm_versions)
            password_to_set = await self.get_password_version(account,good_ver)
            print(f"{account.address};{password_to_set}")
            return await self.set_next_password(account,password_to_set)
        else:
            raise AiobastionException("There is no CPM version for this account")

    # Doc + test
    async def get_password_version(self, account: PrivilegedAccount, version: int):
        data = {"Version": version}
        account_id = await self.get_account_id(account)

        url = f"API/Accounts/{account_id}/Password/Retrieve"

        return await self.epv.handle_request("post", url, data=data)

    async def get_password(self, account: Union[PrivilegedAccount, str, List[PrivilegedAccount], List[str]]):
        """
        Retrieve the password of an address
        :param account: Privileged Account or address id
        :return: Account password value
        """
        return await self.handle_acc_id_list(
            "post",
            lambda account_id: f"API/Accounts/{account_id}/Password/Retrieve",
            await self.get_account_id(account)
        )


    # Test
    async def get_ssh_key(self, account: Union[PrivilegedAccount, str, List[PrivilegedAccount], List[str]]):
        """
        Retrieve the SSH Key of an address
        :param account: Privileged Account or address id
        :return: SSH key value
        """

        return await self.handle_acc_id_list(
            "post",
            lambda account_id: f"API/Accounts/{account_id}/Secret/Retrieve",
            await self.get_account_id(account)
        )

    # Doc + test
    async def get_secret_versions(self, account: Union[PrivilegedAccount, str, List[PrivilegedAccount], List[str]]):
        """
        Retrieve the secret versions
        :param account: Privileged Account or address id
        :return: Account password value
        """
        versions = await self.handle_acc_id_list(
            "get",
            lambda account_id: f"API/Accounts/{account_id}/Secret/Versions/",
            await self.get_account_id(account)
        )

        if isinstance(versions, list):
            return [v["Versions"] for v in versions]
        else:
            return versions["Versions"]

    # Test
    async def get_secret(self, account: Union[PrivilegedAccount, str, List[PrivilegedAccount], List[str]]):
        if isinstance(account, list):
            tasks = []
            for a in account:
                if a.secretType == "key":
                    tasks.append(self.get_ssh_key(a))
                else:
                    tasks.append(self.get_password(a))
            return await asyncio.gather(*tasks)
        else:
            if account.secretType == "key":
                return await self.get_ssh_key(account)
            else:
                return await self.get_password(account)

    async def set_password(self, account, password):
        """
        Set the password for the given address in the vault
        :param account: Privileged address or account_id
        :param password:
        :return: True if success
        """
        return await self.handle_acc_id_list(
            "post",
            lambda account_id: f"API/Accounts/{account_id}/Password/Update",
            await self.get_account_id(account),
            {"NewCredentials": password}
        )

    async def set_next_password(self, account, password):
        """
        Set the password for the given address in the vault
        :param account: Privileged address or account_id
        :param password:
        :return: True if success
        """
        return await self.handle_acc_id_list(
            "post",
            lambda account_id: f"API/Accounts/{account_id}/SetNextPassword",
            await self.get_account_id(account),
            {"ChangeImmediately" : True, "NewCredentials": password}
        )

    async def delete(self, account: Union[PrivilegedAccount, str, List[PrivilegedAccount], List[str]]):
        # account_id = await self.get_account_id(address),
        async def api_call(account_id):
            try:
                return await self.epv.handle_request("delete", f"API/Accounts/{account_id}")
            except CyberarkAPIException:
                return await self.epv.handle_request("delete", f"WebServices/PIMServices.svc/Accounts/{account_id}")

        return await self.handle_acc_list(
            api_call,
            await self.get_account_id(account)
        )

    async def get_cpm_status(self, account: Union[PrivilegedAccount, List[PrivilegedAccount]]):
        if isinstance(account, list):
            return [a.secretManagement for a in account]
        else:
            return account.secretManagement

    async def activity(self, account: Union[PrivilegedAccount, List[PrivilegedAccount]]):
        """
        Get account(s) activity
        """
        activities = await self.handle_acc_id_list(
            "get",
            lambda account_id: f"WebServices/PIMServices.svc/Accounts/{account_id}/Activities/",
            await self.get_account_id(account)
        )

        if isinstance(activities, list):
            return [a["GetAccountActivitiesSlashResult"] for a in activities]
        else:
            return activities["GetAccountActivitiesSlashResult"]

    async def last_cpm_error_message(self, account: Union[PrivilegedAccount, List[PrivilegedAccount]]):
        """
        Get account(s) activity
        """
        activities = await self.activity(account)

        def single_cpm_error(activity):
            for a in activity:
                if "CPM" in a["Activity"]:
                    if "Failure" in a["Reason"]:
                        reason = a["Reason"].split("Error:")
                        return reason[1]

        # List of list
        if any(isinstance(el, list) for el in activities):
            return [single_cpm_error(_activity) for _activity in activities]
        else:
            return single_cpm_error(activities)

    async def add_member_to_group(self, account: Union[PrivilegedAccount, List[PrivilegedAccount]],
                                  group_name: str = "") -> str:
        """
        Add an address to a group
        :param account: a PrivilegedAccount object
        :param group_name: name of the group (or try the address username if empty)
        :return: AccountID
        """
        groups = await self.epv.accountgroup.list_by_safe(account.safeName)
        group_id = 0
        if group_name == "":
            for group in groups:
                if account.userName.lower() in group.name.lower():
                    group_id = group.id
        else:
            for group in groups:
                if group_name.lower() == group.name.lower():
                    group_id = group.id
        if group_id == 0:
            raise AiobastionException("Group name was incorrect of not found")

        async def api_call(acc):
            url = f"API/AccountGroups/{group_id}/Members"
            data = {"AccountId": acc.id}
            return await self.epv.handle_request("post", url, data=data)

        return await self.handle_acc_list(
            api_call,
            account
        )

    async def get_account_group(self, account: Union[PrivilegedAccount, List[PrivilegedAccount]]):
        """
        Returns the GroupID of a given PrivilegedAccount
        :param account: Privileged Account
        :type account: PrivilegedAccount, list
        :return: accountID
        """

        async def api_call(acc):
            for group in await self.epv.accountgroup.list_by_safe(acc.safeName):
                groupid = group.id
                for member in await self.epv.accountgroup.members(groupid):
                    if member.id == acc.id:
                        return groupid
            return None

        return await self.handle_acc_list(api_call, account)

    async def del_account_group_membership(self, account: Union[PrivilegedAccount, List[PrivilegedAccount]]):
        """
        Find AccountGroup for an account_group and delete it
        returns False if no group was remove, True is a group was deleted
        raise an Exception if a group was found but deletion didn't worked
        """

        async def _del_accountgroup(acc):
            groupid = await self.get_account_group(acc)
            if groupid is None:
                return False
            else:
                try:
                    await self.epv.accountgroup.delete_member(acc, groupid)
                except Exception as err:
                    raise CyberarkException("Unable to remove address group " + str(err))
                return True

        return await self.handle_acc_list(_del_accountgroup, account)

    async def update_platform(self, account: Union[PrivilegedAccount, List[PrivilegedAccount]], new_platform: str):
        data = [{"path": "/platformID", "op": "replace", "value": new_platform}]
        return await self.epv.account.update_using_list(account, data)

    async def move(self, account: Union[PrivilegedAccount, List[PrivilegedAccount]], new_safe: str):
        async def _move(acc):
            old_id = acc.id
            acc.safeName = new_safe
            try:
                acc.secret = await self.get_password(acc)
            except CyberarkAPIException as err:
                raise CyberarkException(f"Unable to recover {acc.name} password : {str(err)}")
            try:
                new_account_id = await self.add_account_to_safe(acc)
            except CyberarkAPIException as err:
                raise CyberarkException(f"Unable to create {acc.name} new address : {str(err)}")
            try:
                await self.delete(old_id)
            except CyberarkAPIException as err:
                raise CyberarkException(f"Unable to delete {acc.name} old address : {str(err)}")
            return new_account_id

        return await self.handle_acc_list(_move, account)
