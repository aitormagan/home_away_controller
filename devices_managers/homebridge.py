import requests
from .base import DeviceManager


class HomeBridgeDeviceManager(DeviceManager):

    def __init__(self, host, user, password, devices, port=8581):
        self._host = host
        self._user = user
        self._password = password
        self._devices = devices
        self._port = port
        self._token = None

    def execute_home_away(self):
        for device in self._devices:
            self._set_accessory_status(device["type"], device["id"], device["away_value"])

    def execute_at_home(self):
        for device in self._devices:
            self._set_accessory_status(device["type"], device["id"], device["home_value"])

    def _set_auth_token(self):
        auth_req = requests.post(f"http://{self._host}:{self._port}/api/auth/login",
                                 json={"username": self._user, "password": self._password})
        auth_req.raise_for_status()
        self._token = auth_req.json()["access_token"]

    def _set_accessory_status(self, device_type, device_id, device_status):
        self._execute_request("PUT", f"api/accessories/{device_id}", {
            "characteristicType": device_type,
            "value": device_status
        })

    def _execute_request(self, method, path, body):
        if not self._token:
            self._set_auth_token()

        requests.request(method, f"http://{self._host}:{self._port}/{path}", json=body,
                         headers={"Authorization": f"Bearer {self._token}"}).raise_for_status()
