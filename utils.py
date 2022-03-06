from AllClasses.Dice import Dice
from typing import Union
import tkinter as tk


def listOfDicesToDict(dices: list[Dice]) -> dict[int, int]:
    """
    converts list of dices to dict of added dices
    :param dices: list of dices
    :return: dict with all dices and amount
    """
    result: dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for dice in dices:
        result[dice.get_count()] += 1
    return result


def unique(anyList: list) -> list:
    """
    returns original list, but removes duplicates
    :param anyList: any list
    :return: list without duplicates
    """
    return list(set(anyList))


def grid_helper(elem: Union[tk.Button, tk.Label], row: int, column: int) -> Union[tk.Button, tk.Label]:
    """
    returns object, sets parameter and grid
    :param elem: element to handle
    :param row: row to grid
    :param column: column to grid
    :return: element
    """
    elem.grid(row=row, column=column)
    return elem
