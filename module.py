from abc import ABC, abstractmethod

class Module(ABC):

    @abstractmethod
    def __init__(self, serial=""):
        pass

    @abstractmethod
    def logic(self):
        pass

    @abstractmethod
    def solve(self, input):
        pass