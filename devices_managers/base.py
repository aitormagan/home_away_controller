from abc import ABC, abstractmethod


class DeviceManager(ABC):

    def __init__(self, logger):
        """
        Constructor
        :param logger: Logger
        """
        self._logger = logger

    @property
    def logger(self):
        """
        Returns the logger to be used in case you want your manager to log info
        :return: the logger to be used in case you want your manager to log info
        """
        return self._logger

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
