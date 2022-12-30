from abc import ABC, abstractmethod
from typing import List


class Controller(ABC):

    def __init__(self, logger):
        """
        Constructor
        :param logger: Logger
        """
        self._logger = logger

    @property
    def logger(self):
        """
        Returns the logger to be used in case you want your controller to log info
        :return: the logger to be used in case you want your controller to log info
        """
        return self._logger

    @abstractmethod
    def get_connected_devices(self, hosts: List[str]) -> List[str]:
        """
        Returns the list of connected devices. The list can be (but it's not required) filtered by the hosts passed
        as parameter.
        :param hosts: The list of hosts to be controlled.
        :return: The list of devices which are connected to the network.
        """
        pass
