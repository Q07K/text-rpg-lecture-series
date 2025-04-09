"""입출력 관리 모듈"""


def select_menu(menu):
    while True:
        try:
            num = int(input("선택: "))
            return menu[num - 1]

        except (ValueError, IndexError):
            print("잘못된 입력입니다.")


def hp_bar(unit1, unit2):
    bar_length = 50  # 체력바 길이 (조절 가능)
    unit1_hp = max(0, unit1.hp)
    unit2_hp = max(0, unit2.hp)

    filled_length1 = int((unit1_hp / unit1.max_hp) * bar_length)
    filled_length2 = int((unit2_hp / unit2.max_hp) * bar_length)

    # ⣿ U+28FF
    health_bar1 = "⣿" * filled_length1 + " " * (bar_length - filled_length1)
    health_bar2 = "⣿" * filled_length2 + " " * (bar_length - filled_length2)

    unit1_display = f"[{health_bar1}] {unit1_hp}/{unit1.max_hp}"
    unit2_display = f"[{health_bar2}] {unit2_hp}/{unit2.max_hp}"

    print(unit1.name)
    print(unit1_display)
    print(f"{'':─<52}")
    print(unit2.name)
    print(unit2_display)
