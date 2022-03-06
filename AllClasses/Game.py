from AllClasses.Player import Player


class Game:
    def __init__(self, players: list[Player]):
        self._players: list[Player] = players

        self._current_player: int = 0

    def get_current_player(self) -> Player:
        return self._players[self._current_player]

    def set_new_player(self):
        self._current_player = (self._current_player + 1) % len(self._players)
        self._players[self._current_player].setup()