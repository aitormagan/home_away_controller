from abc import ABC, abstractmethod


class Controller(ABC):

    @abstractmethod
    def get_connected_devices(self):
        pass
