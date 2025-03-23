from modularization import assets

USER = {
    "asset": assets.USER,
    "name": "",
    "level": 1,
    "atk": 1,
    "hp": 10,
    "max_hp": 10,
    "exp": 0,
    "max_exp": 10,
}


def level_up():
    if USER["exp"] < USER["max_exp"]:
        return False

    USER["level"] += 1

    USER["exp"] = USER["exp"] - USER["max_exp"]
    USER["max_exp"] += 10

    USER["max_hp"] += 1
    USER["hp"] = USER["max_hp"]

    USER["atk"] += 1
    return True


def set_user_name():
    print(USER["asset"])
    user_name = input("이름을 입력하세요: ")
    USER["name"] = user_name
