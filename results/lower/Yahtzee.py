from results.Result import Result
from AllClasses.Dice import Dice


class Yahtzee(Result):
    @staticmethod
    def _calc_points(dices: list[Dice]) -> int:
        return 50

    @staticmethod
    def _check(dices: list[Dice]) -> bool:
        return len(list(set([dice.get_count() for dice in dices]))) == 1 and dices[0].get_count() != 0

    @staticmethod
    def get_abbreviation() -> str:
        return "5x"
