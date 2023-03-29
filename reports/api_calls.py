
from connect.client import R
import requests

def request_items(client, product_id) -> dict:
    return client.products[product_id].items.all()
