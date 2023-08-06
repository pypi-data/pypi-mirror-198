from enum import IntFlag
from typing import Any

import requests

from paystack.util import PayStackGatewayFlag, BusinessDataObject, PayStackRestUrl, Command

__all__ = 'list_banks',


class MiscCommandRank(IntFlag):
    LIST_BANKS = 461


def list_banks_cmd(**kwargs) -> Any:
    bdo = BusinessDataObject(use_config=True, **kwargs)
    url = bdo.url(PayStackRestUrl.LIST_BANKS_URL)
    response = requests.get(url=url, headers=bdo.header)
    return response


list_banks = Command(cmd=list_banks_cmd, group=PayStackGatewayFlag.MISCELLANEOUS,
                     rank=MiscCommandRank.LIST_BANKS, label=None)
