import ioka_python
from ioka_python.api_resources.abstract.api_resource import APIResource


class Payment(APIResource):
    GROUP_URL = "/v2/orders"

    @classmethod
    def retrieve(cls, order_id: str, payment_id: str, **params):
        return cls._get(f"{ioka_python.api_host}{cls.GROUP_URL}/{order_id}/payments/{payment_id}", params=params)

    @classmethod
    def create_card(cls, order_id: str, **kwargs):
        return cls._post(f"{ioka_python.api_host}{cls.GROUP_URL}/{order_id}/payments/card", json_obj=kwargs)
