"""출력을 관리하는 모듈"""


def print_menu(frame_size, menu_title, menu_list):
    menu_title = f"[ {menu_title} ]"
    print(f"┌{menu_title:─^{frame_size}}┐")

    for i, data in enumerate(menu_list):
        item = f" {i+1:>2}. {data}"
        print(f"│{item:<{frame_size}}│")

    print(f"└{'':─^{frame_size}}┘")


def appeared(frame_size, asset, name, menu_list):
    name = f"The appearance of {name}"

    print(asset)
    print_menu(frame_size=frame_size, menu_title=name, menu_list=menu_list)


def atk_message(frame_size, attacker):
    menu_title = "[ battle mode ]"

    item = ""
    if attacker:
        item = f"'{attacker['name']}' attacks!"

    print(f"┌{menu_title:─^{frame_size}}┐", flush=True)
    print(f"│{item:^{frame_size}}│", flush=True)
    print(f"└{'':─^{frame_size}}┘", flush=True)


def hp_bar(unit):
    bar_length = 20  # 체력바 길이 (조절 가능)
    filled_length = int((unit["hp"] / unit["max_hp"]) * bar_length)
    health_bar = "⣿" * filled_length + " " * (bar_length - filled_length)
    print(unit["name"], flush=True)
    print(f"[{health_bar}] {unit['hp']}/{unit['max_hp']}", flush=True)


def user_info(frame_size, user):
    print(user["asset"])

    menu_title = f"[ {user['name']} ]"
    print(f"┌{menu_title:─^{frame_size}}┐")

    for key, value in user.items():
        if key in ["asset", "max_hp", "max_exp"]:
            continue
        elif key == "hp":
            value = f"{value}/{user['max_hp']}"
        elif key == "exp":
            value = f"{value}/{user['max_exp']}"

        item = f" {key:<6}: {value}"
        print(f"│{item:<{frame_size}}│")

    print(f"└{'':─^{frame_size}}┘")
