import os
import random
from time import sleep

from text_rpg import assets
from text_rpg.battle import Battle
from text_rpg.io_module import select_menu
from text_rpg.monster import create_monsters
from text_rpg.player import Player
from text_rpg.text_formater import menu_box_num

os.system("cls")  # 화면 지우기

# 초기 화면
print(assets.CLOSE_CASTLE)  # 성문이 닫힌 이미지 출력

# 초기 선택 메뉴
start_menu = ["NEW GAME", "LOAD GAME"]
print(menu_box_num("Game Start", start_menu))  # 메뉴 박스 출력
selected = select_menu(start_menu)  # 선택된 값 반환

# Player 인스턴스 생성
player = Player()

# 선택된 메뉴를 기반으로 조건 처리
if selected == "LOAD GAME":  # LOAD GAME 선택 시
    player.load_file()  # Player `load_file` 메서드 호출
else:
    print(player)  # player asset 출력
    name = input("이름을 입력해 주세요: ")  # 이름 입력 받기
    player.set_name(name)  # Player `set_name` 메서드 호출


# 인게임 선택 메뉴
menu = ["ENTER", "USER INFO", "SAVE", "EXIT"]

# 게임 반복 실행
while True:
    os.system("cls")  # 화면 지우기

    print(assets.CLOSE_CASTLE)  # 성문이 닫힌 이미지 출력
    print(menu_box_num("Battle Start", menu))  # 메뉴 박스 출력
    selected = select_menu(menu)  # 선택된 값 반환

    # 선택된 메뉴를 기반으로 조건 처리
    if selected == "ENTER":  # ENTER 선택 시
        os.system("cls")  # 화면 지우기

        print(assets.OPEN_CASTLE)  # 성문이 열린 이미지 출력
        sleep(1)  # 1초 딜레이

        # Battel 반복 실행
        while True:
            monsters = create_monsters()  # 몬스터 목록 생성
            enemy = random.choice(monsters)  # 랜덤으로 몬스터 선택

            battle = Battle(player=player, enemy=enemy)  # Battle 인스턴스 생성

            # Battle 인스턴스의 `enter` 메서드 값을 기반으로 조건 처리
            if battle.enter():
                battle.start()  # Battle 시작
            else:
                break  # Battle while문 종료

    elif selected == "USER INFO":  # USER INFO 선택 시
        print(player)  # player asset 출력
        print(player.user_info())  # Player 인스턴스의 `user_info` 메서드 호출

        # USER INFO를 나가기 위한 처리
        meue = ["EXIT"]
        print(menu_box_num("EXIT", meue))  # 메뉴 박스 출력
        select_menu(meue)  # 선택된 값 반화
        continue  # 다음 loop

    elif selected == "SAVE":  # SAVE 선택 시
        player.save_file()  # Player 인스턴스의 `save_file` 메서드 호출
        continue  # 다음 loop

    elif selected == "EXIT":  # EXIT 선택 시
        break  # loop 종료
