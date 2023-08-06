from enum import IntFlag
from typing import Any
import requests

from paystack.util import PayStackGatewayFlag, BusinessDataObject, PayStackRestUrl, Command


__all__ = ('fetch_settlements',)


class SettlementCommandRank(IntFlag):
    FETCH_SETTLEMENTS = 239


def fetch_settlements_cmd(**kwargs) -> Any:
    bdo = BusinessDataObject(use_config=True, **kwargs)
    query = bdo.data
    url = bdo.url(PayStackRestUrl.FETCH_SETTLEMENTS_URL)
    return requests.get(url=url, params=query, headers=bdo.header)


fetch_settlements = Command(cmd=fetch_settlements_cmd,
                            group=PayStackGatewayFlag.SETTLEMENTS,
                            rank=SettlementCommandRank.FETCH_SETTLEMENTS, label=None)
