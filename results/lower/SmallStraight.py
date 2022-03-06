from results.Result import Result
from AllClasses.Dice import Dice
from utils import unique
from results.lower.LargeStraight import LargeStraight
import AllClasses.Player

class SmallStraight(Result):
    _options: list[list[int]] = [
        [1,2,3,4],
        [2,3,4,5],
        [3,4,5,6]
    ]
    @staticmethod
    def _calc_points(dices: list[Dice]) -> int:
        return 30

    @staticmethod
    def _check(dices: list[Dice]) -> bool:
        return unique([x.get_count() for x in dices]) in SmallStraight._options \
               or AllClasses.Player.Player(dices=dices).get_result_by_type(LargeStraight).is_result()

    @staticmethod
    def get_abbreviation() -> str:
        return "SStreet"
