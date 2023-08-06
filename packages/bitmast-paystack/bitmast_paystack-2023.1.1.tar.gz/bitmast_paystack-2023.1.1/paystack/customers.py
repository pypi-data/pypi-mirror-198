import json
from enum import IntFlag
from typing import Any

import requests

from paystack.util import PayStackGatewayFlag, BusinessDataObject, \
    PayStackRestUrl, Command

__all__ = ('create_customer', 'list_customers', 'fetch_customer', 'update_customer',
           'whitelist_customer', 'blacklist_customer')


class CustomerCommandRank(IntFlag):
    CREATE = 2
    LIST_CUSTOMERS = 3
    FETCH = 5
    UPDATE = 7
    WHITELIST_CUSTOMER = 11
    BLACKLIST_CUSTOMER = 13
    DEACTIVATE_AUTHORIZATION = 17


class CustomerBusinessObject(BusinessDataObject):
    def __init__(self, **kwargs):
        super(CustomerBusinessObject, self).__init__(**kwargs)


def create_customer_cmd(**kwargs) -> Any:
    bdo = kwargs.pop('config')
    if not isinstance(bdo, BusinessDataObject):
        raise ValueError('Invalid Business Data Object')
    bdo.update(**kwargs)
    data = bdo.data
    url = bdo.url(PayStackRestUrl.CREATE_CUSTOMER_URL)
    response = requests.post(url, data=json.dumps(data), headers=bdo.header)

    return response


def list_customers_cmd(**kwargs) -> Any:
    bdo = kwargs.pop('config')
    if not isinstance(bdo, BusinessDataObject):
        raise ValueError('Invalid Business Data Object')
    bdo.update(**kwargs)
    query = bdo.data
    url = bdo.url(PayStackRestUrl.LIST_CUSTOMERS_URL, params=query)
    response = requests.get(url=url, headers=bdo.header)

    return response


def fetch_customer_cmd(**kwargs) -> Any:
    bdo = kwargs.pop('config')
    if not isinstance(bdo, BusinessDataObject):
        raise ValueError('Invalid Business Data Object')
    bdo.update(**kwargs)
    url = bdo.url(PayStackRestUrl.FETCH_CUSTOMER_URL)
    customer_id = bdo.data.get('customer_id')
    url += f'{customer_id}/'
    response = requests.get(url, headers=bdo.header)

    return response


def update_customer_cmd(**kwargs) -> Any:
    bdo = kwargs.pop('config')
    if not isinstance(bdo, BusinessDataObject):
        raise ValueError('Invalid Business Data Object')
    bdo.update(**kwargs)
    data = bdo.data
    url = bdo.url(PayStackRestUrl.UPDATE_CUSTOMER_URL)
    response = requests.put(url, data=json.dumps(data), headers=bdo.header)

    return response


def customer_access_control_cmd(**kwargs) -> Any:
    bdo = kwargs.pop('config')
    if not isinstance(bdo, BusinessDataObject):
        raise ValueError('Invalid Business Data Object')
    bdo.update(**kwargs)
    data = bdo.data
    url = bdo.url(PayStackRestUrl.CUSTOMER_ACCESS_CONTROL_URL)
    response = requests.post(url, data=json.dumps(data), headers=bdo.header)

    return response


create_customer = Command(cmd=create_customer_cmd, group=PayStackGatewayFlag.CUSTOMERS,
                          rank=CustomerCommandRank.CREATE, label=None)
list_customers = Command(cmd=list_customers_cmd, group=PayStackGatewayFlag.CUSTOMERS,
                         rank=CustomerCommandRank.LIST_CUSTOMERS, label=None)
fetch_customer = Command(cmd=fetch_customer_cmd, group=PayStackGatewayFlag.CUSTOMERS,
                         rank=CustomerCommandRank.FETCH, label=None)
update_customer = Command(cmd=update_customer_cmd, group=PayStackGatewayFlag.CUSTOMERS,
                          rank=CustomerCommandRank.UPDATE, label=None)
whitelist_customer = Command(cmd=customer_access_control_cmd,
                             group=PayStackGatewayFlag.CUSTOMERS,
                             rank=CustomerCommandRank.UPDATE, label=None)
blacklist_customer = Command(cmd=customer_access_control_cmd,
                             group=PayStackGatewayFlag.CUSTOMERS,
                             rank=CustomerCommandRank.UPDATE, label=None)
