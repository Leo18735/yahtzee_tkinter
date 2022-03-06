from results.Result import Result
from AllClasses.Dice import Dice
from utils import listOfDicesToDict

class FourOfAKind(Result):
    @staticmethod
    def _calc_points(dices: list[Dice]) -> int:
        return sum([dice.get_count() for dice in dices])

    @staticmethod
    def _check(dices: list[Dice]) -> bool:
        dictionary: dict = listOfDicesToDict(dices)
        for number in dictionary.keys():
            if dictionary[number] >= 4:
                return True
        return False

    @staticmethod
    def get_abbreviation() -> str:
        return "4x"
