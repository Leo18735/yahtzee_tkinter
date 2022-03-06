from results.Result import Result, Dice
from utils import listOfDicesToDict


class Six(Result):
    @staticmethod
    def _calc_points(dices: list[Dice]) -> int:
        return listOfDicesToDict(dices)[6] * 6

    @staticmethod
    def _check(dices: list[Dice]) -> bool:
        return True

    @staticmethod
    def get_abbreviation() -> str:
        return "6"
