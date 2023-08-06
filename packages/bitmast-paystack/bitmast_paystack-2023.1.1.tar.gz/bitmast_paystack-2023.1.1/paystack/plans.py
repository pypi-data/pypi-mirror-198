import json
from enum import IntFlag
from typing import Any
import requests

from paystack.util import PayStackGatewayFlag, BusinessDataObject, PayStackRestUrl, Command


__all__ = ('create_plan', 'list_plans', 'update_plan', 'fetch_plan')


class PlanCommandRank(IntFlag):
    CREATE_PLAN = 79
    LIST_PLANS = 83
    FETCH_PLAN = 89
    UPDATE_PLAN = 97


def create_plan_cmd(**kwargs) -> Any:
    bdo = BusinessDataObject(use_config=True, **kwargs)
    data = bdo.data
    url = bdo.url(PayStackRestUrl.CREATE_PLAN_URL)
    response = requests.post(url=url, data=json.dumps(data), headers=bdo.header)
    
    return response


def list_plans_cmd(**kwargs) -> Any:
    bdo = BusinessDataObject(use_config=True, **kwargs)
    query = bdo.data
    url = bdo.url(PayStackRestUrl.LIST_PLANS_URL)
    response = requests.get(url=url, params=query, headers=bdo.header)
    
    return response


def fetch_plan_cmd(**kwargs) -> Any:
    bdo = BusinessDataObject(use_config=True, **kwargs)
    data = bdo.data
    url = bdo.url(PayStackRestUrl.FETCH_PRODUCT_URL)
    plan_id = data.get('plan_id') or data.get('id') or data.get('slug') or data.get('code')
    url += f'{plan_id}'
    response = requests.post(url=url, headers=bdo.header)
    
    return response


def update_plan_cmd(**kwargs) -> Any:
    bdo = BusinessDataObject(use_config=True, **kwargs)
    data = bdo.data
    plan_id = data.get('plan_id') or data.get('id_or_code') or data.get('slug')
    url = bdo.url(PayStackRestUrl.UPDATE_PRODUCT_URL)
    url += f'{plan_id}'
    if 'plan_id' in data:
        del data['plan_id']
    elif 'id_or_code' in data:
        del data['id_or_code']
    elif 'slug' in data:
        del data['slug']
    response = requests.put(url=url, data=json.dumps(data), headers=bdo.header)
    
    return response


create_plan = Command(cmd=create_plan_cmd, group=PayStackGatewayFlag.PLANS,
                      rank=PlanCommandRank.CREATE_PLAN, label=None)
list_plans = Command(cmd=list_plans_cmd, group=PayStackGatewayFlag.PLANS,
                     rank=PlanCommandRank.LIST_PLANS, label=None)
fetch_plan = Command(cmd=fetch_plan_cmd, group=PayStackGatewayFlag.PLANS,
                     rank=PlanCommandRank.FETCH_PLAN, label=None)
update_plan = Command(cmd=update_plan_cmd, group=PayStackGatewayFlag.PLANS,
                      rank=PlanCommandRank.UPDATE_PLAN, label=None)
