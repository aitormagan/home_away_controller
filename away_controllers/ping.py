import subprocess
from .base import Controller


class PingController(Controller):

    def get_connected_devices(self, hosts):
        return list(filter(lambda x: self._ping(x), hosts))

    @staticmethod
    def _ping(host):
        return subprocess.call(['ping', "-c", '1', host]) == 0
