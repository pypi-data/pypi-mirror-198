import json
from enum import IntFlag
from typing import Any

import requests

from paystack.util import PayStackGatewayFlag, PayStackRestUrl, BusinessDataObject, Command

__all__ = ('create_subaccount', 'list_subaccounts', 'fetch_subaccount', 'update_subaccount',
           'AccountCommandRank')


class AccountCommandRank(IntFlag):
    CREATE = 2
    LIST_SUBACCOUNTS = 3
    FETCH = 5
    UPDATE = 7


def create_subaccount_cmd(**kwargs) -> Any:
    bdo = BusinessDataObject(use_config=True, **kwargs)
    url = bdo.url(PayStackRestUrl.CREATE_SUBACCOUNT_URL)
    response = requests.post(url=url, json=bdo.data, headers=bdo.header)
    return response


def list_subaccount_cmd(**kwargs) -> Any:
    bdo = BusinessDataObject(use_config=True, **kwargs)
    query_data = bdo.data
    url = bdo.url(PayStackRestUrl.LIST_SUBACCOUNTS_URL)
    response = requests.get(url=url, params=query_data, headers=bdo.header)
    return response


def fetch_subaccount_cmd(**kwargs) -> Any:
    bdo = BusinessDataObject(use_config=True, **kwargs)
    url = bdo.url(PayStackRestUrl.FETCH_SUBACCOUNT_URL)
    account_id = bdo.data.get('account_id') or bdo.data.get('id_or_code')
    url += f'{account_id}/'
    response = requests.get(url=url, headers=bdo.header)
    return response


def update_subaccount_cmd(**kwargs) -> Any:
    bdo = BusinessDataObject(use_config=True, **kwargs)
    data = bdo.data
    url = bdo.url(PayStackRestUrl.UPDATE_SUBACCOUNT_URL)
    response = requests.put(url, data=json.dumps(data), headers=bdo.header)
    return response


create_subaccount = Command(cmd=create_subaccount_cmd, group=PayStackGatewayFlag.SUBACCOUNTS,
                            rank=AccountCommandRank.CREATE, label=None)

list_subaccounts = Command(cmd=list_subaccount_cmd, group=PayStackGatewayFlag.SUBACCOUNTS,
                           rank=AccountCommandRank.LIST_SUBACCOUNTS, label=None)

fetch_subaccount = Command(cmd=fetch_subaccount_cmd, group=PayStackGatewayFlag.SUBACCOUNTS,
                           rank=AccountCommandRank.CREATE, label=None)

update_subaccount = Command(cmd=create_subaccount_cmd,
                            group=PayStackGatewayFlag.SUBACCOUNTS,
                            rank=AccountCommandRank.UPDATE, label=None)
