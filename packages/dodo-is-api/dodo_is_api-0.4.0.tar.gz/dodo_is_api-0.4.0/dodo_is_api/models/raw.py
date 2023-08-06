from typing import TypedDict

__all__ = (
    'StopSaleTypedDict',
    'StopSaleByIngredientTypedDict',
    'StopSaleBySalesChannelTypedDict',
    'StopSaleByProductTypedDict',
    'UnitDeliveryStatisticsTypedDict',
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


class UnitDeliveryStatisticsTypedDict(TypedDict):
    unitId: str
    unitName: str
    deliverySales: int
    deliveryOrdersCount: int
    avgDeliveryOrderFulfillmentTime: int
    avgCookingTime: int
    avgHeatedShelfTime: int
    avgOrderTripTime: int
    lateOrdersCount: int
    tripsCount: int
    tripsDuration: int
    couriersShiftsDuration: int
    ordersWithCourierAppCount: int
