"""Battle 관리 모듈"""

from time import sleep

from text_rpg.io_module import hp_bar, select_menu


class Battle:
    """Battle Class"""

    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def enter(self):
        menu = ["Attack", "Run"]
        print(self.enemy.appeared(menu))
        selected = select_menu(menu)

        return selected == "Attack"

    def display_battle(self):
        print(self.enemy)
        hp_bar(self.enemy, self.player)
        sleep(1)

    def take_turn(self):
        self.player >> self.enemy
        self.display_battle()
        if self.enemy.is_dead():
            self.player.exp += self.enemy.exp
            self.player.level_up()
            return False

        self.enemy >> self.player
        self.display_battle()
        if self.player.is_dead():
            return False

        return True

    def start(self):
        self.display_battle()

        while self.take_turn():
            pass
