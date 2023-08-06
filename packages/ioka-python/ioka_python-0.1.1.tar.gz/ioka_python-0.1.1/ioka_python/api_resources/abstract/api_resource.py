from collections import namedtuple

import requests

import ioka_python


class APIResource:
    @classmethod
    def get_ioka_object(cls, response_data):
        if isinstance(response_data, list):
            return [cls.get_ioka_object(instance) for instance in response_data]
        return namedtuple('ioka_object', response_data.keys())(*response_data.values())

    @classmethod
    def request_call(cls, method, url, **kwargs):
        return_object = error = None
        headers = {"API-KEY": ioka_python.api_key}
        try:
            response = requests.request(method, url, headers=headers, **kwargs)
            response.raise_for_status()
            return_object = cls.get_ioka_object(response.json())
        except requests.exceptions.HTTPError as http_error:
            error = f"Http Error: {http_error}"
        except requests.exceptions.ConnectionError as connection_error:
            error = f"Error Connecting: {connection_error}"
        except requests.exceptions.Timeout as timeout_error:
            error = f"Timeout Error: {timeout_error}"
        except requests.exceptions.RequestException as request_error:
            error = f"OOps: Something Else: {request_error}"
        if error is not None:
            raise Exception(error)
        return return_object

    @classmethod
    def _get(cls, url: str, params: dict):
        return cls.request_call("get", url, params=params)

    @classmethod
    def _post(cls, url: str, json_obj: dict):
        return cls.request_call("post", url, json=json_obj)

    @classmethod
    def _delete(cls, url: str, json_obj: dict):
        return cls.request_call("delete", url, json=json_obj)
