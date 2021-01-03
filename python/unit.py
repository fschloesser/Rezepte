
unit_list = [
        "st",
        "g",
        "ml",
        "EL",
        "TL",
        ]

class unit:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

for u in unit_list:
    var = unit(u)
    globals()[u] = var
