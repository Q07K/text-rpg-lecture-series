"""텍스트 포맷 관리 모듈"""


def make_box_title(title):
    title_str = f"[ {title} ]"
    top = f"┌{title_str:─^50}┐"
    bottom = f"└{'':─^50}┘"
    return top, bottom


def menu_box(title, data):
    top, bottom = make_box_title(title)

    result = ""
    for key, value in data.items():
        line = f" {key:<6}: {value}"
        line = f"│{line:<50}│"
        result += line + "\n"

    return top + "\n" + result + bottom


def menu_box_num(title, data):
    top, bottom = make_box_title(title)

    result = ""
    for idx, value in enumerate(data):
        line = f" {idx+1:>2}. {value}"
        line = f"│{line:<50}│"
        result += line + "\n"

    return top + "\n" + result + bottom
