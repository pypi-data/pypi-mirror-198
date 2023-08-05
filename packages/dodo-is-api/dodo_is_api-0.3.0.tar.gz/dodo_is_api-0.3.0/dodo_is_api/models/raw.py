from typing import TypedDict

__all__ = (
    'StopSaleTypedDict',
    'StopSaleByIngredientTypedDict',
    'StopSaleBySalesChannelTypedDict',
    'StopSaleByProductTypedDict',
)


class StopSaleTypedDict(TypedDict):
    id: str
    unitId: str
    unitName: str
    reason: str
    startedAt: str
    endedAt: str | None
    stoppedByUserId: str
    resumedByUserId: str | None


class StopSaleBySalesChannelTypedDict(StopSaleTypedDict):
    salesChannelName: str
    channelStopType: str


class StopSaleByIngredientTypedDict(StopSaleTypedDict):
    ingredientName: str


class StopSaleByProductTypedDict(StopSaleTypedDict):
    productName: str
