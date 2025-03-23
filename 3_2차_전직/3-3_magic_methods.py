class Player:

    # 생성자
    def __init__(self, name):
        self.name = name
        self.hp = 10
        self.max_hp = 10
        self.atk = 1
        self.exp = 0
        self.max_exp = 100
        self.level = 1

    # repr / print
    def __repr__(self):
        return f"Player: {self.name}"

    # -
    def __sub__(self, other):
        if isinstance(other, Monster):
            self.hp -= other.atk


class Monster:

    # 생성자
    def __init__(self, name, hp, exp, atk):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.atk = atk
        self.exp = exp

    # repr / print
    def __repr__(self):
        return f"Monster: {self.name}"

    # ==
    def __eq__(self, other):
        return True

    # =!
    def __ne__(self, other):
        return False

    # +
    def __add__(self, other):
        pass

    # -
    def __sub__(self, other):
        if isinstance(other, Player):
            self.hp -= other.atk


player = Player(name="player")
print(f"{player = }")
slime = Monster(name="slime", hp=10, exp=10, atk=1)
print(f"{slime = }")
print()

print("전투 시작!")
for i in range(10):
    print(f"turn {i + 1}")
    player - slime
    print(f"{player.hp = }")
    slime - player
    print(f"{slime.hp = }")
    print()
