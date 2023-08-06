import json
from enum import IntFlag
from typing import Any
import requests

from paystack.util import PayStackGatewayFlag, BusinessDataObject, PayStackRestUrl, Command


__all__ = ('resolve_bvn', 'bvn_match', 'resolve_account_number', 'resolve_card_bin',
           'resolve_phone_number')


class VerificationCommandRank(IntFlag):
    RESOLVE_BVN = 433
    BVN_MATCH = 439
    RESOLVE_ACCOUNT_NUMBER = 443
    RESOLVE_CARD_BIN = 449
    RESOLVE_PHONE_NUMBER = 457


def resolve_bvn_cmd(**kwargs) -> Any:
    bdo = BusinessDataObject(use_config=True, **kwargs)
    data = bdo.data
    bvn = data.get('bvn') or data.get('bank_verification_number')
    url = bdo.url(PayStackRestUrl.RESOLVE_BVN_URL)
    url += f'{bvn}'
    response = requests.get(url=url, headers=bdo.header)
    
    return response


def bvn_match_cmd(**kwargs) -> Any:
    bdo = BusinessDataObject(use_config=True, **kwargs)
    data = bdo.data
    url = bdo.url(PayStackRestUrl.BVN_MATCH_URL)
    response = requests.post(url=url, data=json.dumps(data), headers=bdo.header)
    
    return response


def resolve_account_number_cmd(**kwargs) -> Any:
    bdo = BusinessDataObject(use_config=True, **kwargs)
    data = bdo.data
    url = bdo.url(PayStackRestUrl.RESOLVE_ACCOUNT_NUMBER_URL)
    response = requests.get(url=url, params=data, headers=bdo.header)
    
    return response


def resolve_card_bin_cmd(**kwargs) -> Any:
    bdo = BusinessDataObject(use_config=True, **kwargs)
    data = bdo.data
    card_bin = data.get('card_bin') or data.get('bin')
    url = bdo.url(PayStackRestUrl.RESOLVE_CARD_BIN_URL)
    url += f'{card_bin}'
    response = requests.put(url=url, data=json.dumps(data), headers=bdo.header)
    
    return response


def resolve_phone_number_cmd(**kwargs) -> Any:
    bdo = BusinessDataObject(use_config=True, **kwargs)
    data = bdo.data
    url = bdo.url(PayStackRestUrl.RESOLVE_PHONE_NUMBER_URL)
    response = requests.post(url=url, data=json.dumps(data), headers=bdo.header)
    
    return response


resolve_bvn = Command(cmd=resolve_bvn_cmd, group=PayStackGatewayFlag.VERIFICATION,
                      rank=VerificationCommandRank.RESOLVE_BVN, label=None)
bvn_match = Command(cmd=bvn_match_cmd, group=PayStackGatewayFlag.VERIFICATION,
                    rank=VerificationCommandRank.BVN_MATCH, label=None)
resolve_account_number = Command(cmd=resolve_account_number_cmd,
                                 group=PayStackGatewayFlag.VERIFICATION,
                                 rank=VerificationCommandRank.RESOLVE_ACCOUNT_NUMBER,
                                 label=None)
resolve_card_bin = Command(cmd=resolve_card_bin_cmd, group=PayStackGatewayFlag.VERIFICATION,
                           rank=VerificationCommandRank.RESOLVE_CARD_BIN, label=None)

resolve_phone_number = Command(cmd=resolve_phone_number_cmd,
                               group=PayStackGatewayFlag.VERIFICATION,
                               rank=VerificationCommandRank.RESOLVE_CARD_BIN, label=None)
