"""Player 관리 모듈"""

import os
from time import sleep

from text_rpg import assets
from text_rpg.text_formater import menu_box


class Player:
    def __init__(self):
        self.name = ""
        self.asset = assets.PLAYER
        self.level = 1
        self.atk = 1
        self.hp = 10
        self.max_hp = 10
        self.exp = 0
        self.max_exp = 10

    def set_name(self, name):
        self.name = name

    def __repr__(self):
        os.system("cls")
        return self.asset

    def user_info(self):
        hp = f"{self.hp}/{self.max_hp}"
        exp = f"{self.exp}/{self.max_exp}"

        data = {
            "NAME": self.name,
            "LEVEL": self.level,
            "HP": hp,
            "ATK": self.atk,
            "EXP": exp,
        }

        return menu_box(self.name, data)

    def save_file(self):
        with open(file="Text-RPG.txt", mode="w", encoding="utf-8") as f:
            f.write(self.name + "\n")
            f.write(str(self.level) + "\n")
            f.write(str(self.atk) + "\n")
            f.write(str(self.hp) + "\n")
            f.write(str(self.max_hp) + "\n")
            f.write(str(self.exp) + "\n")
            f.write(str(self.max_exp) + "\n")

    def load_file(self):
        with open(file="Text-RPG.txt", mode="r", encoding="utf-8") as f:
            self.name = f.readline().strip()
            self.level = int(f.readline())
            self.atk = int(f.readline())
            self.hp = int(f.readline())
            self.max_hp = int(f.readline())
            self.exp = int(f.readline())
            self.max_exp = int(f.readline())

    def level_up(self):
        if self.exp < self.max_exp:
            return

        self.level += 1
        self.atk += 1
        self.max_hp += 1
        self.hp = self.max_hp
        self.exp -= self.max_exp
        self.max_exp += 10
        os.system("cls")
        print(assets.LEVEL_UP)
        sleep(1)

    def attack(self, monster):
        monster.hp -= self.atk

    def __sub__(self, monster):
        self.attack(monster)

    def is_dead(self):
        if self.hp <= 0:
            self.hp = 0
            return True
        return False
