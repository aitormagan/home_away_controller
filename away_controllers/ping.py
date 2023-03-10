from typing import List
import subprocess
from .base import Controller


class PingController(Controller):

    def __init__(self, logger):
        """
        Ping Controller constructor
        :param logger: Logger
        """
        super().__init__(logger)

    def get_connected_devices(self, hosts: List[str]) -> List[str]:
        return list(filter(lambda x: self._ping(x), hosts))

    @staticmethod
    def _ping(host: str):
        return subprocess.call(['ping', "-c", '1', host]) == 0
