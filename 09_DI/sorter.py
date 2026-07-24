
from abc import ABC
from abc import abstractmethod


class Sorter(ABC):
    @abstractmethod
    def sort(self, data):
        pass
