import requests
import json
import os

URL = os.getenv("QE_API_SERVER")

def login():
    """
    "username": "logim.test",
    "service_name": "LOGIYO"
    으로 로그인
    """
    response = requests.request("GET", f"http://{URL}/api/dispatch/login/",)
    return json.loads(response.text)

def cancel_order_or_dispatched(type: str, rider_id, headers):
    """
    주문취소, 배차취소

    CANCLE_ORDER - 주문 취소
    CANCLE_DISPATCH - 배차 취소
    CANCLE_ORDER_AFTER_COMPLETED - 배달완료 후 주문취소
    """

    return json.loads(requests.request("POST", f"http://{URL}/api/dispatch/cancel_order/",
                     json={'type': type.upper(), 'rider_id': rider_id, 'headers': headers}).text)