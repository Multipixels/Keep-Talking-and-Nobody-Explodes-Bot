from _typeshed import NoneType


from abc import ABC, abstractmethod

class Module(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def logic(self):
        pass

    @abstractmethod
    def solve(self, input):
        pass