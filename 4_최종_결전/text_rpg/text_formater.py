"""텍스트 포맷 관리 모듈"""


def menu_box(title, data):
    title = f"[ {title} ]"
    title = f"┌{title:─^50}┐"
    bottom = f"└{'':─^50}┘"

    result = ""
    for key, value in data.items():
        line = f" {key:<6}: {value}"
        line = f"│{line:<50}│"
        result += line + "\n"

    return title + "\n" + result + bottom


def menu_box_num(title, data):
    title = f"[ {title} ]"
    title = f"┌{title:─^50}┐"
    bottom = f"└{'':─^50}┘"

    result = ""
    for idx, value in enumerate(data):
        line = f" {idx+1:>2}. {value}"
        line = f"│{line:<50}│"
        result += line + "\n"

    return title + "\n" + result + bottom
