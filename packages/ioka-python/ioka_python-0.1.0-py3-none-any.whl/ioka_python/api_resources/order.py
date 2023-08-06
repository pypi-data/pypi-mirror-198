import ioka_python
from ioka_python.api_resources.abstract.api_resource import APIResource


class Order(APIResource):
    GROUP_API_URL = "/v2/orders"

    @classmethod
    def list(cls, **params):
        return cls._get(f"{ioka_python.api_host}{cls.GROUP_API_URL}", params=params)

    @classmethod
    def retrieve(cls, order_id: str, **params):
        return cls._get(f"{ioka_python.api_host}{cls.GROUP_API_URL}/{order_id}", params=params)

    @classmethod
    def list_events(cls, order_id: str, **params):
        return cls._get(f"{ioka_python.api_host}{cls.GROUP_API_URL}/{order_id}/events", params=params)

    @classmethod
    def list_refunds(cls, order_id: str, **params):
        return cls._get(f"{ioka_python.api_host}{cls.GROUP_API_URL}/{order_id}/refunds", params=params)

    @classmethod
    def retrieve_refund(cls, order_id: str, refund_id: str, **params):
        return cls._get(f"{ioka_python.api_host}{cls.GROUP_API_URL}/{order_id}/refunds/{refund_id}", params=params)

    @classmethod
    def create(cls, **kwargs):
        return cls._post(f"{ioka_python.api_host}{cls.GROUP_API_URL}", json_obj=kwargs)

    @classmethod
    def capture(cls, order_id: str, **kwargs):
        return cls._post(f"{ioka_python.api_host}{cls.GROUP_API_URL}/{order_id}/capture", json_obj=kwargs)

    @classmethod
    def cancel(cls, order_id: str, **kwargs):
        return cls._post(f"{ioka_python.api_host}{cls.GROUP_API_URL}/{order_id}/cancel", json_obj=kwargs)

    @classmethod
    def refund(cls, order_id: str, **kwargs):
        return cls._post(f"{ioka_python.api_host}{cls.GROUP_API_URL}/{order_id}/refund", json_obj=kwargs)
