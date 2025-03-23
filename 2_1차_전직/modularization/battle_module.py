import os
import time

from modularization.input_module import selete_menu
from modularization.print_module import appeared, atk_message, hp_bar


def atk(attacker, defender):
    defender["hp"] -= attacker["atk"]
    defender["hp"] = max(defender["hp"], 0)


def is_alive(defender):
    return bool(defender["hp"])


def battle(user, enemy):
    os.system("cls")

    data_list = ["Fight", "Run away"]
    appeared(
        frame_size=50,
        asset=enemy["asset"],
        name=enemy["name"],
        menu_list=data_list,
    )
    seleted = selete_menu(menu_list=data_list)

    if seleted == "Fight":
        os.system("cls")

        print(enemy["asset"])

        atk_message(frame_size=50, attacker="")
        hp_bar(unit=user)
        hp_bar(unit=enemy)
        time.sleep(0.5)

    while seleted == "Fight":
        os.system("cls")
        atk(attacker=user, defender=enemy)
        print(enemy["asset"])

        atk_message(frame_size=50, attacker=user)
        hp_bar(unit=user)
        hp_bar(unit=enemy)

        time.sleep(1)
        if not is_alive(defender=enemy):
            user["exp"] += enemy["exp"]

            enemy["hp"] = enemy["max_hp"]
            break

        os.system("cls")
        atk(attacker=enemy, defender=user)
        print(enemy["asset"])

        atk_message(frame_size=50, attacker=enemy)
        hp_bar(unit=user)
        hp_bar(unit=enemy)

        time.sleep(1)
        if not is_alive(defender=user):
            break
