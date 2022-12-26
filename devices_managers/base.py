from abc import ABC, abstractmethod


class DeviceManager(ABC):

    @abstractmethod
    def execute_home_away(self):
        pass

    @abstractmethod
    def execute_at_home(self):
        pass
