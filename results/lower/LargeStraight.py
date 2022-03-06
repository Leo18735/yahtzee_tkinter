from results.Result import Result
from AllClasses.Dice import Dice
from utils import unique


class LargeStraight(Result):
    _options: list[list[int]] = [
        [1,2,3,4,5],
        [2,3,4,5,6]
    ]
    @staticmethod
    def _calc_points(dices: list[Dice]) -> int:
        return 40

    @staticmethod
    def _check(dices: list[Dice]) -> bool:
        return unique([x.get_count() for x in dices]) in LargeStraight._options

    @staticmethod
    def get_abbreviation() -> str:
        return "LStreet"
