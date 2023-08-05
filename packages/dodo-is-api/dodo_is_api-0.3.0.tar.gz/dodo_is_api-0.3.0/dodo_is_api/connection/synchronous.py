import datetime
from collections.abc import Iterable, Generator
from uuid import UUID

import httpx

from .base import BaseConnection, concatenate_uuids, raise_for_status
from ..models import raw as raw_models

__all__ = ('DodoISAPIConnection',)


class DodoISAPIConnection(BaseConnection):
    __slots__ = ('__http_client',)

    def __init__(self, *, http_client: httpx.Client):
        self.__http_client = http_client

    def iter_late_delivery_vouchers(
            self,
            *,
            from_date: datetime.datetime,
            to_date: datetime.datetime,
            units: Iterable[UUID],
            skip: int = 0,
            take: int = 1000,
    ) -> Generator[list[dict], None, None]:
        url = '/delivery/vouchers'
        request_query_params = {
            'from': from_date.strftime('%Y-%m-%dT%H:%M:%S'),
            'to': to_date.strftime('%Y-%m-%dT%H:%M:%S'),
            'units': concatenate_uuids(units),
            'skip': skip,
            'take': take,
        }

        while True:
            response = self.__http_client.get(url, params=request_query_params)
            raise_for_status(response)

            response_data = response.json()
            yield response_data['vouchers']
            if response_data['isEndOfListReached']:
                break
            request_query_params['skip'] += take

    def get_stop_sales_by_ingredients(
            self,
            *,
            from_date: datetime.datetime,
            to_date: datetime.datetime,
            units: Iterable[UUID],
    ) -> list[raw_models.StopSaleByIngredientTypedDict]:
        """
        References:
            Documentation: https://dodo-brands.stoplight.io/docs/dodo-is/846af18915ab3-proizvodstvo-stop-prodazhi-po-ingredientam

        Keyword Args:
            from_date: start of period in ISO 8601 format.
            to_date: end of period in ISO 8601 format.
            units: collection of unit's UUIDs.

        Returns:
            List of stop sales by ingredients.
        """
        url = '/production/stop-sales-ingredients'
        request_query_params = {
            'from': from_date.strftime('%Y-%m-%dT%H:%M:%S'),
            'to': to_date.strftime('%Y-%m-%dT%H:%M:%S'),
            'units': concatenate_uuids(units),
        }
        response = self.__http_client.get(url, params=request_query_params)
        raise_for_status(response)

        response_data: dict = response.json()
        return response_data['stopSalesByIngredients']

    def get_stop_sales_by_sales_channels(
            self,
            *,
            from_date: datetime.datetime,
            to_date: datetime.datetime,
            units: Iterable[UUID],
    ) -> list[raw_models.StopSaleBySalesChannelTypedDict]:
        """
        References:
            Documentation: https://dodo-brands.stoplight.io/docs/dodo-is/6bcaeb26e9f28-proizvodstvo-stop-prodazhi-po-kanalam-prodazh

        Keyword Args:
            from_date: start of period in ISO 8601 format.
            to_date: end of period in ISO 8601 format.
            units: collection of unit's UUIDs.

        Returns:
            List of stop sales by sales channels.
        """
        url = '/production/stop-sales-channels'
        request_query_params = {
            'from': from_date.strftime('%Y-%m-%dT%H:%M:%S'),
            'to': to_date.strftime('%Y-%m-%dT%H:%M:%S'),
            'units': concatenate_uuids(units),
        }
        response = self.__http_client.get(url, params=request_query_params)
        raise_for_status(response)

        response_data: dict = response.json()
        return response_data['stopSalesBySalesChannels']

    def get_stop_sales_by_products(
            self,
            *,
            from_date: datetime.datetime,
            to_date: datetime.datetime,
            units: Iterable[UUID],
    ) -> list[raw_models.StopSaleByProductTypedDict]:
        """
        References:
            Documentation: https://dodo-brands.stoplight.io/docs/dodo-is/f90f05153cfac-proizvodstvo-stop-prodazhi-po-produktam

        Keyword Args:
            from_date: start of period in ISO 8601 format.
            to_date: end of period in ISO 8601 format.
            units: collection of unit's UUIDs.

        Returns:
            List of stop sales by products.
        """
        url = '/production/stop-sales-products'
        request_query_params = {
            'from': from_date.strftime('%Y-%m-%dT%H:%M:%S'),
            'to': to_date.strftime('%Y-%m-%dT%H:%M:%S'),
            'units': concatenate_uuids(units),
        }
        response = self.__http_client.get(url, params=request_query_params)
        raise_for_status(response)

        response_data: dict = response.json()
        return response_data['stopSalesByProducts']
