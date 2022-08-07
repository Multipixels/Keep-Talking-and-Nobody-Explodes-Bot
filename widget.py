from abc import ABC, abstractmethod

class Widget(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def getValue(self):
        pass

    @abstractmethod
    def setValue(self):
        pass