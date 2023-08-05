import datetime
import enum
from dataclasses import dataclass
from uuid import UUID

__all__ = (
    'LateDeliveryVoucher',
    'StopSale',
    'StopSaleByProduct',
    'StopSaleByIngredient',
    'StopSaleBySalesChannel',
    'SalesChannel',
    'ChannelStopType',
)


@dataclass(frozen=True, slots=True)
class LateDeliveryVoucher:
    order_id: UUID
    order_number: str
    order_accepted_at_local: datetime.datetime
    unit_uuid: UUID
    predicted_delivery_time_local: datetime.datetime
    order_fulfilment_flag_at_local: datetime.datetime | None
    delivery_deadline_local: datetime.datetime
    issuer_name: str | None
    courier_staff_id: UUID | None


class SalesChannel(str, enum.Enum):
    DINE_IN = 'Dine-in'
    TAKEAWAY = 'Takeaway'
    DELIVERY = 'Delivery'


class ChannelStopType(str, enum.Enum):
    COMPLETE = 'Complete'
    REDIRECTION = 'Redirection'


@dataclass(frozen=True, slots=True)
class StopSale:
    id: UUID
    unit_uuid: UUID
    unit_name: str
    reason: str
    started_at: datetime.datetime
    ended_at: datetime.datetime | None
    stopped_by_user_id: UUID
    resumed_by_user_id: UUID | None


@dataclass(frozen=True, slots=True)
class StopSaleBySalesChannel(StopSale):
    sales_channel_name: SalesChannel
    channel_stop_type: ChannelStopType


@dataclass(frozen=True, slots=True)
class StopSaleByIngredient(StopSale):
    ingredient_name: str


@dataclass(frozen=True, slots=True)
class StopSaleByProduct(StopSale):
    product_name: str
