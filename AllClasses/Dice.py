import random
from typing import Union


class Dice:
    def __init__(self):
        self._count: int = 0
        self._keep: bool = False

    def __lt__(self, other) -> bool:
        return self.get_count() < other.get_count()

    def roll(self) -> Union[bool, int]:
        if self._keep:
            return False
        self._count = random.randrange(1, 7)
        return self._count

    def get_count(self) -> int:
        return self._count

    def toggle_keep(self) -> None:
        self._keep = not self._keep

    def get_keep(self) -> bool:
        return self._keep
