import os
import random
from time import sleep

from text_rpg import assets
from text_rpg.battle import Battle
from text_rpg.io_module import select_menu
from text_rpg.monster import create_monsters
from text_rpg.player import Player
from text_rpg.text_formater import menu_box_num

os.system("cls")
start_menu = ["NEW GAME", "LOAD GAME"]
print(assets.CLOSE_CASTLE)
print(menu_box_num("Game Start", start_menu))
selected = select_menu(start_menu)

player = Player()
if selected == "LOAD GAME":
    player.load_file()
else:
    print(player)
    name = input("이름을 입력해 주세요: ")
    player.set_name(name)

menu = ["ENTER", "USER INFO", "SAVE", "EXIT"]
while True:
    os.system("cls")
    print(assets.CLOSE_CASTLE)
    print(menu_box_num("Battle Start", menu))
    selected = select_menu(menu)

    if selected == "ENTER":
        os.system("cls")
        print(assets.OPEN_CASTLE)
        sleep(1)

        while True:
            monsters = create_monsters()
            enemy = random.choice(monsters)

            battle = Battle(player=player, enemy=enemy)
            if battle.enter():
                battle.start()
            else:
                break

    elif selected == "USER INFO":
        print(player)
        print(player.user_info())
        print(menu_box_num("EXIT", ["EXIT"]))
        select_menu(["EXIT"])

    elif selected == "SAVE":
        player.save_file()
        continue

    elif selected == "EXIT":
        break
