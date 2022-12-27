from abc import ABC, abstractmethod


class DeviceManager(ABC):

    @abstractmethod
    def execute_home_away(self):
        """
        The method to be executed when there is no one at home.
        :return: None
        """
        pass

    @abstractmethod
    def execute_at_home(self):
        """
        The method to be executed when there is at least one person at home.
        :return: None
        """
        pass
