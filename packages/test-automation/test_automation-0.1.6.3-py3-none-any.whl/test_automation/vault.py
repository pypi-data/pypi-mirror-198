import requests
import json
import os

URL = os.getenv("QE_API_SERVER")

def get_path_value(path):
    response = requests.get(f"http://{URL}/api/vault?path={path}")
    return json.loads(response.text)

def get_key_value(path, key) :
    response = requests.get(f"http://{URL}/api/vault?path={path}&key={key}")
    return json.loads(response.text)
