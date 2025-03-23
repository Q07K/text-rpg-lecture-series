"""게임을 실행하는 모듈"""

import os
import time

from modularization import assets, monster
from modularization.battle_module import battle
from modularization.input_module import selete_menu
from modularization.player import USER, level_up, set_user_name
from modularization.print_module import print_menu, user_info


def main():
    os.system("cls")
    set_user_name()
    os.system("cls")

    enter_menu = ["enter", "exit", "user_info"]

    while True:
        print(assets.CLOSE_CASTLE)
        print_menu(frame_size=50, menu_title="GAME MENU", menu_list=enter_menu)
        selete = selete_menu(menu_list=enter_menu)

        if selete == "enter":
            os.system("cls")
            print(assets.OPEN_CASTLE)

            time.sleep(1)
            battle(user=USER, enemy=monster.SLIME)
            if level_up():
                os.system("cls")
                print(assets.LEVEL_UP)
                time.sleep(0.5)

        elif selete == "exit":
            os.system("cls")
            return
        elif selete == "user_info":
            os.system("cls")
            user_info(50, USER)

            exit_data = ["exit"]

            print_menu(
                frame_size=50,
                menu_title="USER INFO MENU",
                menu_list=exit_data,
            )

            selete = selete_menu(menu_list=exit_data)
            if selete == "exit":
                os.system("cls")

        os.system("cls")


if __name__ == "__main__":
    main()
