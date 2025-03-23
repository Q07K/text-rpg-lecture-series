"""텍스트 입력을 관리하는 모듈"""


def selete_menu(menu_list):
    select = input("선택: ")

    if select.isdigit():
        select = int(select)
        if 0 < select <= len(menu_list):
            return menu_list[select - 1]

    return ""
