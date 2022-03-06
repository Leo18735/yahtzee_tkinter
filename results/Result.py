from abc import ABC, abstractmethod
from AllClasses.Dice import Dice
import AllClasses.Player

class Result(ABC):
    def __init__(self, player, gathered: int = None):
        self._points_gathered: int = -1 if not gathered else gathered
        self._player: AllClasses.Player.Player = player

    @staticmethod
    @abstractmethod
    def _calc_points(dices: list[Dice]) -> int:
        pass

    def is_result(self) -> int:
        return self._calc_points(self._player.get_dices()) if self._check(self._player.get_dices()) else 0

    @staticmethod
    @abstractmethod
    def _check(dices: list[Dice]) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def get_abbreviation() -> str:
        pass

    def get_points_gathered(self) -> int:
        return self._points_gathered

    def select(self) -> bool:
        if self._points_gathered != -1:
            return False
        self._points_gathered = self.is_result()
        return True
