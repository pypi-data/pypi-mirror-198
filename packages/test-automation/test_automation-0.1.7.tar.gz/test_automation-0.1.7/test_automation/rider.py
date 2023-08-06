import requests
import json
import os

URL = os.getenv("QE_API_SERVER")


def login(email_address, password, phone_number):
    response = requests.request("POST", f"http://{URL}/api/rideryo/login/", json={
        'email_address': email_address,
        'password': password,
        "phone_number": phone_number
    })

    return json.loads(response.text)


def verify_start_work(lat, lng, headers):
    """
    :param lat: 라이더 시작 위치 lat
    :param lng: 라이더 시작 위치 lng
    :param headers: 로그인 후 header 정보
    :return: zone_id, zone_name
    """
    response = requests.request("POST", f"http://{URL}/api/rideryo/verify_start_work/", json={
        "lat": lat,
        "lng": lng,
        "headers": headers
    })

    jsonObject = json.loads(response.text)

    return jsonObject['zone_id'], jsonObject['zone_name']


def start_work(zone_id, zone_name, lat, lng, headers):
    response = requests.request("POST", f"http://{URL}/api/rideryo/start_work/", json={
        "zone_id": zone_id,
        "zone_name": zone_name,
        "lat": lat,
        "lng": lng,
        "headers": headers
    })

    return json.loads(response.text)


def break_off(zone_id, zone_name, lat, lng, headers):
    response = requests.request("POST", f"http://{URL}/api/rideryo/break_off/", json={
        "zone_id": zone_id,
        "zone_name": zone_name,
        "lat": lat,
        "lng": lng,
        "headers": headers
    })

    return json.loads(response.text)


def update_location(lat, lng, headers):
    response = requests.request("POST", f"http://{URL}/api/rideryo/update_location/", json={
        "lat": lat,
        "lng": lng,
        "headers": headers
    })

    return json.loads(response.text)


def rider_id(zone_id, rider_name, headers):
    """
    :param zone_id: zone_id
    :param rider_name:  profile_summary 를 통해 라이더 이름 가져오기
    :param headers: 로그인 후 header 값
    :return: rider_id 값
    """

    response = requests.request("POST", f"http://{URL}/api/rideryo/rider_id/", json={
        "zone_id": zone_id,
        "rider_name": rider_name,
        "headers": headers
    })

    print(response.text)

    return json.loads(response.text)


def profile_summary(headers):
    """
    :param headers: 로그인 후 header 값
    :return: 라이더 Full name
    """
    response = requests.request("POST", f"http://{URL}/api/rideryo/profile_summary/", json={
        "headers": headers
    })

    return json.loads(response.text)


def rider_state_ready(headers):
    response = requests.request("POST", f"http://{URL}/api/rideryo/state/", json={
        "headers": headers
    })

    return json.loads(response.text)


def prepare_ready_for_working(email_address, password, phone_number, lat, lng):
    """
    로그인(문자인증) -> 라이더 업무시작 준비 -> 업무시작 -> break_off 진행
    :param email_address:   로그인 계정 아이디
    :param password:    로그인 계정 비밀번호
    :param phone_number:    로그인 계정 핸드폰 번호
    :param lat: 라이더 시작 위치 lat
    :param lng: 라이더 시작 위치 lng
    :return: rider_id 값, headers 값
    """

    headers = login(email_address, password, phone_number)
    zone_id, zone_name = verify_start_work(lat, lng, headers)
    start_work(zone_id, zone_name, lat, lng, headers)
    break_off(zone_id, zone_name, lat, lng, headers)
    update_location(lat, lng, headers)

    return rider_id(zone_id, profile_summary(headers), headers), headers


def logout(headers):
    response = requests.request("POST", f"http://{URL}/api/rideryo/logout/", json={
        "headers": headers
    })

    if json.loads(response.text)['success']:
        return True
    else:
        return False


def stop_work(headers):
    response = requests.request("POST", f"http://{URL}/api/rideryo/stop_work/", json={
        "headers": headers
    })

    if json.loads(response.text)['success']:
        return True
    else:
        return False


def pulling_dispatched(headers):
    response = requests.request("POST", f"http://{URL}/api/rideryo/pulling_dispatched/", json={
        "headers": headers
    })

    return json.loads(response.text)


def dispatches(dispatch_id, headers):
    response = requests.request("POST", f"http://{URL}/api/rideryo/dispatches/", json={
        "dispatch_id": dispatch_id,
        "headers": headers
    })

    return json.loads(response.text)


def delivery_state(dispatch_id, state, headers):
    response = requests.request("POST", f"http://{URL}/api/rideryo/delivery_state/", json={
        "dispatch_id": dispatch_id,
        "state": state,
        "headers": headers
    })

    return json.loads(response.text)


def rider_route(headers):
    response = requests.request("POST", f"http://{URL}/api/rideryo/rider_route/", json={
        "headers": headers
    })

    return json.loads(response.text)


def dispatch_response(dispatch_id, response, headers):
    response = requests.request("POST", f"http://{URL}/api/rideryo/dispatch_response/", json={
        "dispatch_id": dispatch_id,
        "response": response,
        "headers": headers
    })

    return json.loads(response.text)


def dispatch_id(delivery_id, headers):
    response = requests.request("POST", f"http://{URL}/api/rideryo/return_dispatch_id/", json={
        "delivery_id" : delivery_id,
        "headers" : headers
    })

    return json.loads(response.text)
