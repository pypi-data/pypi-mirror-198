import ioka_python
from ioka_python.api_resources.abstract.api_resource import APIResource


class Customer(APIResource):
    GROUP_URL = "/v2/customers"

    @classmethod
    def list(cls, **params):
        return cls._get(f"{ioka_python.api_host}{cls.GROUP_URL}", params=params)

    @classmethod
    def retrieve(cls, customer_id: str, **params):
        return cls._get(f"{ioka_python.api_host}{cls.GROUP_URL}/{customer_id}", params=params)

    @classmethod
    def list_events(cls, customer_id: str, **params):
        return cls._get(f"{ioka_python.api_host}{cls.GROUP_URL}/{customer_id}/events", params=params)

    @classmethod
    def create(cls, **kwargs):
        return cls._post(f"{ioka_python.api_host}{cls.GROUP_URL}", json_obj=kwargs)

    @classmethod
    def delete(cls, customer_id: str, **kwargs):
        return cls._delete(f"{ioka_python.api_host}{cls.GROUP_URL}/{customer_id}", json_obj=kwargs)
