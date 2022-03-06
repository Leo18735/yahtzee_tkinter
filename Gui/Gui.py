import tkinter as tk
from utils import grid_helper
from functools import partial
from typing import Union

from AllClasses.Game import Game
from AllClasses.Player import Player

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



class Gui:
    def __init__(self, root: tk.Tk = tk.Tk()):
        self._root: tk.Tk = root

        self._currentPlayerNameLabel: tk.Label
        self._triesLabel: tk.Label
        self._currentPlayerPointsLabel: tk.Label

        self._buttons: dict[str, Union[Result, tk.Button]] = {}
        self._dice_buttons: list[tk.Button] = []

        player = Player("Simon")

        cache: dict[str, list[Result]] = {
            "upper": [
                One(player, 3),
                Two(player, 6),
                Three(player, 9),
                Four(player, 12),
                Five(player, 15),
                Six(player, 18),
                Bonus(player)
            ], "lower": [
                ThreeOfAKind(player),
                FourOfAKind(player),
                FullHouse(player),
                SmallStraight(player),
                LargeStraight(player),
                Chance(player),
                Yahtzee(player)
            ]
        }

        player.set_results(cache)

        playerNames: list[Player] = [
            player,
            Player("Max")]
        self._game: Game = Game(playerNames)

        self._setup()


    def _setup(self):

        row: int = 0

        tk.Label(self._root, text="Player: ").grid(row=row, column=0)
        self._currentPlayerNameLabel = grid_helper(tk.Label(self._root), row=row, column=1)
        self._currentPlayerPointsLabel = grid_helper(tk.Label(self._root), row=row, column=2)

        row += 1

        tk.Label(self._root).grid(row=row, column=0)  # placeholder

        row += 1

        for iterator in range(len(self._game.get_current_player().get_results())):
            if iterator % 3 == 0:
                row += 1
            self._buttons.update({self._game.get_current_player().get_results()[iterator].get_abbreviation(): {"result": None, "button": grid_helper(tk.Button(self._root,
                                                            command=partial(self._select, iterator)),
                                                            row=row,
                                                            column=iterator % 3)}})

        row += 1

        tk.Label(self._root).grid(row=row, column=0)  # placeholder

        row += 1
        for i in range(5):
            self._dice_buttons.append(grid_helper(tk.Button(self._root, text="0", command=partial(self._toggleKeep, i)),
                                                  row=row, column=i))

        row += 1

        tk.Label(self._root, text="Versuche:").grid(row=row, column=0)
        self._triesLabel = grid_helper(tk.Label(self._root), row=row, column=1)
        tk.Button(self._root, text="Würfeln", command=self._roll_dices).grid(row=row, column=2)

        self._set_new_player()

    def _select(self, result_count: int):
        if self._game.get_current_player().select(result_count):
            self._set_new_player()

    def run(self):
        self._root.mainloop()

    def _check(self):
        for result in self._game.get_current_player().get_results():
            result_points: int = result.is_result() if result.get_points_gathered() == -1 else result.get_points_gathered()
            if result.get_points_gathered() != -1:
                color = "purple"
            elif result_points == 0:
                color = "red"
            elif result_points != 0:
                color = "green"
            else:
                color = "white"
            if result.get_points_gathered() != -1:
                a = 0
            self._buttons[result.get_abbreviation()]["button"].configure(text=f"{result.get_abbreviation()}: "
                                                                              f"{result_points}", bg=color)

    def _set_new_player(self):
        self._game.set_new_player()
        self._currentPlayerNameLabel.configure(text=self._game.get_current_player().get_name())
        self._currentPlayerPointsLabel.configure(text=self._game.get_current_player().get_points())
        self._triesLabel.configure(text=self._game.get_current_player().get_rolls())

        for result in self._game.get_current_player().get_results():
            self._buttons[result.get_abbreviation()].update({"result": result})

        self._set_dices()

    def _roll_dices(self):
        if self._game.get_current_player().get_rolls() == 0:
            return
        else:
            self._game.get_current_player().roll()
        self._triesLabel.configure(text=self._game.get_current_player().get_rolls())

        self._set_dices()

    def _set_dices(self):
        for dice in range(len(self._game.get_current_player().get_dices())):
            self._dice_buttons[dice].configure(text=self._game.get_current_player().get_dices()[dice].get_count())
            self._dice_buttons[dice].configure(bg="green" if
                self._game.get_current_player().get_dices()[dice].get_keep() else "red")

        self._check()

    def _toggleKeep(self, dice_count: int):
        self._game.get_current_player().toggle_dice(dice_count)
        self._dice_buttons[dice_count].configure(bg="green" if
                self._game.get_current_player().get_dices()[dice_count].get_keep() else "red")
