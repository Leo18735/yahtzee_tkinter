import AllClasses.Player
from results.Result import Result, Dice


class Bonus(Result):
    def __init__(self, player):
        super().__init__(player=player)
        self._points_gathered: int = 0
    @staticmethod
    def _calc_points(dices: list[Dice]) -> int:
        return 35

    def _check(self, _: list[Dice]) -> bool:
        return sum([x.get_points_gathered() for x in self._player.get_upper()]) >= 63

    @staticmethod
    def get_abbreviation() -> str:
        return "B"

    def select(self) -> bool:
        self._points_gathered = self.is_result()
        return False