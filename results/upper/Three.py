from results.Result import Result, Dice
from utils import listOfDicesToDict


class Three(Result):
    @staticmethod
    def _calc_points(dices: list[Dice]) -> int:
        return listOfDicesToDict(dices)[3] * 3

    @staticmethod
    def _check(dices: list[Dice]) -> bool:
        return True

    @staticmethod
    def get_abbreviation() -> str:
        return "3"
