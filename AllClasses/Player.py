from AllClasses.Dice import Dice


from results.Result import Result
# upper
from results.upper.One import One
from results.upper.Two import Two
from results.upper.Three import Three
from results.upper.Four import Four
from results.upper.Five import Five
from results.upper.Six import Six
from results.upper.Bonus import Bonus
# lower
from results.lower.Chance import Chance
from results.lower.FourOfAKind import FourOfAKind
from results.lower.FullHouse import FullHouse
from results.lower.LargeStraight import LargeStraight
from results.lower.SmallStraight import SmallStraight
from results.lower.ThreeOfAKind import ThreeOfAKind
from results.lower.Yahtzee import Yahtzee


class Player:
    def __init__(self, name: str = "Unknown", dices: list[Dice] = None):
        self._dices: list[Dice] = dices if dices else []
        self._name: str = name
        self._rolls: int = 0

        self._results: dict[str, list[Result]] = {
            "upper": [
                One(self),
                Two(self),
                Three(self),
                Four(self),
                Five(self),
                Six(self),
                Bonus(self)
            ], "lower": [
                ThreeOfAKind(self),
                FourOfAKind(self),
                FullHouse(self),
                SmallStraight(self),
                LargeStraight(self),
                Chance(self),
                Yahtzee(self)
            ]
        }

    def get_results(self) -> list[Result]:
        cache: list = []
        for value in self._results.values():
            cache += value
        return cache

    def get_upper(self):
        return self._results["upper"]

    def get_result_by_type(self, result_type: any) -> Result:
        for result in self.get_results():
            if type(result) == result_type:
                return result

    def select(self, result_count) -> bool:
        self.get_result_by_type(Bonus).select()
        return self.get_results()[result_count].select()

    def roll(self):
        self._rolls -= 1
        for dice in self._dices:
            dice.roll()
        self._dices.sort()

    def get_rolls(self):
        return self._rolls

    def setup(self):
        self._dices = [Dice(), Dice(), Dice(), Dice(), Dice()]
        self._rolls = 3

    def get_name(self):
        return self._name
    def get_dices(self) -> list[Dice]:
        return self._dices
    def toggle_dice(self, dice_count: int):
        self._dices[dice_count].toggle_keep()
    def get_points(self) -> int:
        return sum([x.get_points_gathered() for x in self.get_results() if x.get_points_gathered() != -1])
