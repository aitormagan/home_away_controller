import requests
from .base import DeviceManager


class HomeBridgeDeviceManager(DeviceManager):

    def __init__(self, host, user, password, devices, logger, port=8581):
        """
        HomeBridge Constructor.
        :param host: HomeBridge IP.
        :param user: The username used to connect with HomeBridge (generally `admin`).
        :param password: The password used to connect with HomeBridge.
        :param devices: A list with all the devices whose state should be modified when arriving/leaving home. For each
        one:
        * id: The unique HomeBridge ID attached to the device.
        * type: The type of the device (`On`, `TargetHeatingCoolingState`, etc.)
        * away_value: The value to be set to the device when leaving home. None for no action.
        * home_value: The value to be set to the device when arriving home. None for no action.
        :param port: The HomeBridge port (generally `8581`)
        :param logger: Logger
        """
        super().__init__(logger)
        self._host = host
        self._user = user
        self._password = password
        self._devices = devices
        self._port = port
        self._token = None

    def execute_home_away(self):
        self._execute_generic("away_value")

    def execute_at_home(self):
        self._execute_generic("home_value")

    def _execute_generic(self, value_key):
        for device in self._devices:
            if device[value_key] is not None:
                self._set_accessory_status(device["type"], device["id"], device[value_key])

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
