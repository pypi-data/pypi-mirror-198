from datetime import datetime
from typing import NoReturn
from uuid import UUID

from . import models
from .models import raw as raw_models

__all__ = (
    'map_late_delivery_voucher_dto',
    'map_stop_sale_by_sales_channel_dto',
    'map_stop_sale_by_product_dto',
    'map_stop_sale_by_ingredient_dto',
)


def parse_to_datetime_or_none(value: str | None) -> datetime | None | NoReturn:
    match value:
        case str():
            return datetime.fromisoformat(value)
        case None:
            return
        case _:
            raise ValueError('Invalid type')


def parse_to_uuid_or_none(value: str | None) -> UUID | None | NoReturn:
    match value:
        case str():
            return UUID(value)
        case None:
            return
        case _:
            raise ValueError('Invalid type')


def map_late_delivery_voucher_dto(late_delivery_voucher: dict) -> models.LateDeliveryVoucher:
    return models.LateDeliveryVoucher(
        order_id=UUID(late_delivery_voucher['orderId']),
        order_number=late_delivery_voucher['orderNumber'],
        order_accepted_at_local=datetime.fromisoformat(late_delivery_voucher['orderAcceptedAtLocal']),
        unit_uuid=UUID(late_delivery_voucher['unitId']),
        predicted_delivery_time_local=datetime.fromisoformat(late_delivery_voucher['predictedDeliveryTimeLocal']),
        order_fulfilment_flag_at_local=parse_to_datetime_or_none(late_delivery_voucher['orderFulfilmentFlagAtLocal']),
        delivery_deadline_local=datetime.fromisoformat(late_delivery_voucher['deliveryDeadlineLocal']),
        issuer_name=late_delivery_voucher['issuerName'],
        courier_staff_id=parse_to_uuid_or_none(late_delivery_voucher['courierStaffId']),
    )


def map_stop_sale_by_sales_channel_dto(
        stop_sale_by_sales_channel: raw_models.StopSaleBySalesChannelTypedDict,
) -> models.StopSaleBySalesChannel:
    return models.StopSaleBySalesChannel(
        id=UUID(stop_sale_by_sales_channel['id']),
        unit_uuid=UUID(stop_sale_by_sales_channel['unitId']),
        unit_name=stop_sale_by_sales_channel['unitName'],
        reason=stop_sale_by_sales_channel['reason'],
        stopped_by_user_id=UUID(stop_sale_by_sales_channel['stoppedByUserId']),
        resumed_by_user_id=parse_to_uuid_or_none(stop_sale_by_sales_channel['resumedByUserId']),
        started_at=datetime.fromisoformat(stop_sale_by_sales_channel['startedAt']),
        ended_at=parse_to_datetime_or_none(stop_sale_by_sales_channel['endedAt']),
        sales_channel_name=models.SalesChannel(stop_sale_by_sales_channel['salesChannelName']),
        channel_stop_type=models.ChannelStopType(stop_sale_by_sales_channel['channelStopType']),
    )


def map_stop_sale_by_ingredient_dto(
        stop_sale_by_ingredient: raw_models.StopSaleByIngredientTypedDict,
) -> models.StopSaleByIngredient:
    return models.StopSaleByIngredient(
        id=UUID(stop_sale_by_ingredient['id']),
        unit_uuid=UUID(stop_sale_by_ingredient['unitId']),
        unit_name=stop_sale_by_ingredient['unitName'],
        reason=stop_sale_by_ingredient['reason'],
        stopped_by_user_id=UUID(stop_sale_by_ingredient['stoppedByUserId']),
        resumed_by_user_id=parse_to_uuid_or_none(stop_sale_by_ingredient['resumedByUserId']),
        started_at=datetime.fromisoformat(stop_sale_by_ingredient['startedAt']),
        ended_at=parse_to_datetime_or_none(stop_sale_by_ingredient['endedAt']),
        ingredient_name=stop_sale_by_ingredient['ingredientName'],
    )


def map_stop_sale_by_product_dto(
        stop_sale_by_product: raw_models.StopSaleByProductTypedDict,
) -> models.StopSaleByProduct:
    return models.StopSaleByProduct(
        id=UUID(stop_sale_by_product['id']),
        unit_uuid=UUID(stop_sale_by_product['unitId']),
        unit_name=stop_sale_by_product['unitName'],
        reason=stop_sale_by_product['reason'],
        stopped_by_user_id=UUID(stop_sale_by_product['stoppedByUserId']),
        resumed_by_user_id=parse_to_uuid_or_none(stop_sale_by_product['resumedByUserId']),
        started_at=datetime.fromisoformat(stop_sale_by_product['startedAt']),
        ended_at=parse_to_datetime_or_none(stop_sale_by_product['endedAt']),
        product_name=stop_sale_by_product['productName'],
    )
