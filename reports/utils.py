import datetime
from reports import api_calls

BASE_CURRENCY = 'USD'
FOREXAPI_URL = 'https://theforexapi.com/api/latest'


def get_complex_value(base, search_array, default_value='-') -> str:
    try:
        if len(search_array) == 1:
            return base[search_array[0]]
        print(search_array[0])
        print(base[search_array[0]])
        return get_complex_value(base[search_array[0]], search_array[1:])
    except Exception as ex:
        return default_value


def get_basic_value(base, value):
    try:
        if base and value in base:
            return base[value]
        return '-'
    except Exception:
        return '-'