from abc import ABC, abstractmethod


class Controller(ABC):

    @abstractmethod
    def get_connected_devices(self, hosts):
        """
        Returns the list of connected devices. The list can be (but it's not required) filtered by the hosts passed
        as parameter.
        :param hosts: The list of hosts to be controlled.
        :return: The list of devices which are connected to the network.
        """
        pass
