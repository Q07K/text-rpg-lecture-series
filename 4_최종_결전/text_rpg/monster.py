"""Monster 관리 모듈"""

import os

from text_rpg import assets
from text_rpg.text_formater import menu_box_num


class Monster:
    def __init__(self, name, asset, atk, hp, exp):
        self.name = name
        self.asset = asset
        self.atk = atk
        self.hp = hp
        self.max_hp = hp
        self.exp = exp

    def __repr__(self):
        os.system("cls")
        return self.asset

    def appeared(self, menu):
        os.system("cls")
        title = f"'{self.name}' appears!"
        return self.asset + "\n" + menu_box_num(title, menu)

    def attack(self, player):
        player.hp -= self.atk

    def __rshift__(self, player):
        self.attack(player)

    def is_dead(self):
        if self.hp <= 0:
            self.hp = 0
            return True
        return False


SLIME = {
    "name": "Slime",
    "asset": assets.SLIME,
    "atk": 1,
    "hp": 10,
    "exp": 10,
}

CAT = {
    "name": "Cat",
    "asset": assets.CAT,
    "atk": 2,
    "hp": 20,
    "exp": 20,
}


def create_monsters():
    slime = Monster(**SLIME)
    cat = Monster(**CAT)
    return [slime, cat]
