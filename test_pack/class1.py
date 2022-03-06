from abc import ABC, abstractmethod


class Class1(ABC):
    @classmethod
    def hi(cls):
        return cls._hi2()

    @staticmethod
    @abstractmethod
    def _hi2() -> str:
        pass
