from results.Result import Result
from AllClasses.Dice import Dice


class Chance(Result):
    @staticmethod
    def _calc_points(dices: list[Dice]) -> int:
        return sum([dice.get_count() for dice in dices])

    @staticmethod
    def _check(dices: list[Dice]) -> bool:
        return True

    @staticmethod
    def get_abbreviation() -> str:
        return "Cha"
