from results.Result import Result
from AllClasses.Dice import Dice
from utils import listOfDicesToDict

class FullHouse(Result):
    @staticmethod
    def _calc_points(dices: list[Dice]) -> int:
        return 25

    @staticmethod
    def _check(dices: list[Dice]) -> bool:
        dictionary: dict = listOfDicesToDict(dices)
        for number in dictionary:
            if dictionary[number] == 3:
                for number2 in dictionary:
                    if dictionary[number2] == 2:
                        return True
        return False

    @staticmethod
    def get_abbreviation() -> str:
        return "3x2"
