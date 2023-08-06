import json
from enum import IntFlag
from typing import Any
import requests

from paystack.util import PayStackGatewayFlag, BusinessDataObject, PayStackRestUrl, Command


__all__ = ('create_product', 'list_products', 'update_product', 'fetch_product')


class ProductCommandRank(IntFlag):
    CREATE_PRODUCT = 127
    LIST_PRODUCTS = 131
    FETCH_PRODUCT = 137
    UPDATE_PRODUCT = 139


def create_product_cmd(**kwargs) -> Any:
    bdo = BusinessDataObject(use_config=True, **kwargs)
    data = bdo.data
    url = bdo.url(PayStackRestUrl.CREATE_PRODUCT_URL)
    response = requests.post(url=url, data=json.dumps(data), headers=bdo.header)
    
    return response


def list_products_cmd(**kwargs) -> Any:
    bdo = BusinessDataObject(use_config=True, **kwargs)
    url = bdo.url(PayStackRestUrl.LIST_PRODUCTS_URL)
    response = requests.get(url=url, headers=bdo.header)
    
    return response


def fetch_product_cmd(**kwargs) -> Any:
    bdo = BusinessDataObject(use_config=True, **kwargs)
    data = bdo.data
    url = bdo.url(PayStackRestUrl.FETCH_PRODUCT_URL)
    product_id = data.get('product_id') or data.get('id') or data.get('slug')
    url += f'{product_id}'
    response = requests.post(url=url, headers=bdo.header)
    
    return response


def update_product_cmd(**kwargs) -> Any:
    bdo = BusinessDataObject(use_config=True, **kwargs)
    data = bdo.data
    product_id = data.get('product_id') or data.get('id') or data.get('slug')
    url = bdo.url(PayStackRestUrl.UPDATE_PRODUCT_URL)
    url += f'{product_id}'
    if 'product_id' in data:
        del data['product_id']
    elif 'id' in data:
        del data['id']
    elif 'slug' in data:
        del data['slug']
    response = requests.put(url=url, data=json.dumps(data), headers=bdo.header)
    
    return response


create_product = Command(cmd=create_product_cmd, group=PayStackGatewayFlag.PRODUCTS,
                         rank=ProductCommandRank.CREATE_PRODUCT, label=None)
list_products = Command(cmd=list_products_cmd, group=PayStackGatewayFlag.PRODUCTS,
                        rank=ProductCommandRank.LIST_PRODUCTS, label=None)
fetch_product = Command(cmd=fetch_product_cmd, group=PayStackGatewayFlag.PRODUCTS,
                        rank=ProductCommandRank.FETCH_PRODUCT, label=None)
update_product = Command(cmd=update_product_cmd, group=PayStackGatewayFlag.PRODUCTS,
                         rank=ProductCommandRank.UPDATE_PRODUCT, label=None)
