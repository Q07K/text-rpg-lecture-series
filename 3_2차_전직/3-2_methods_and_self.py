class Unit:
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


unit_a = Unit()
unit_a.set_name("a")

unit_b = Unit()
unit_b.set_name("b")

print(f"{unit_a.get_name() = }")
print(f"{unit_b.get_name() = }")
