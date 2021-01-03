
unit_list = [
        [ "st", "Stueck", "", ""],
        [ "g", "g", "gr", "gr"],
        [ "ml", "ml", "ml", "ml"],
        [ "el", "EL", "tbsp", "cda"],
        [ "tl", "TL", "tsp", "cdta"],
        [ "pse", "Prise", "pinch", "pizca"],
        [ "tasse", "Tasse", "cup", "taza"],
        ]

class unit:

    def __init__(self, u):
        self.name = u[0]
        self.german = u[1]
        self.english = u[2]
        self.spanish = u[3]

    def __str__(self):
        return self.name

for u in unit_list:
    var = unit(u)
    globals()[var.name] = var
    del var
