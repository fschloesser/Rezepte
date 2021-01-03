
from unit import *

food_list = [
        ["eier", 10, st],
        ["mehl", 20, g],
        ["zucker", 30, g],
        ["maismehl", 40, g],
        ]

class food:

    def __init__(self, name, cals, unit=st):
        self.name = name
        self.cals = cals
        self.unit = unit

    def __str__(self):
        return self.name


for x, y, z in food_list:
    var = food(x, y, z)
    globals()[x] = var

