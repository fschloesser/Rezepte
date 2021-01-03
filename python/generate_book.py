
class unit:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


unit_list = ["st", "g", "ml"]

for u in unit_list:
    var = unit(u)
    globals()[u] = var


class food:

    def __init__(self, name, cals, unit=st):
        self.name = name
        self.cals = cals
        self.unit = unit

    def __str__(self):
        return self.name


food_list = [
        ["eier", 10, st],
        ["mehl", 20, g],
        ]

for x, y, z in food_list:
    var = food(x, y, z)
    globals()[x] = var


class ingredient:

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return self.name


class rezept:

    def __init__(self, title, subtitle):
        self.title = title
        self.subtitle = subtitle
        self.spacing = self.space(title)
        self.steps = []
        self.ingredients = []
        self.notes = []

    def __str__(self):
        if len(self.ingredients) == 0 or len(self.steps) == 0:
            return ""

        return "rezept\{{title}\}\{{spacing}, {cals} kcal\}\{{subtitle}\}\{{ingredients}\}\{{instructions}\}".format(
                title=self.title,
                cals=self.cals(),
                subtitle=self.subtitle,
                ingredients=self.get_ingredients(),
                instructions=self.get_instructions())

    def space(self, title):
        return 20

    def cals(self):
        return sum([i.cals for i in self.ingredients])

    def get_ingredients(self):
        return self.ingredients

    def get_instructions(self):
        return "\n\n".join(self.steps + ["Notiz: {n}".format(n) for n in self.notes])

    def schritt(self, step):
        self.steps.append(step)
        return self

    def notiz(self, note):
        self.notes.append(note)
        return self

    def add(self, quantity, food):
        self.ingredients.append(ingredient(quantity, food))
        return self


class book:

    def __init__(self):
        self.recipes = []

    def __str__(self):
        return "Book: {}".format(["Rezept: {}".format(r) for r in self.recipes()])

    def add(self, rec):
        self.recipes.append(rec)


b = book()

bisquit = rezept("Bisquit", "sehr fluffy, gut zu schneiden, 1655 kcal")
bisquit.add(6, eier).add(150, zucker).add(90, mehl).add(30, maismehl)

bisquit.schritt("""
Eier und Zucker über einem Wasserbad vermischen bis der Zucker sich aufgelöst hat, das Ei soll nicht stocken.
Vom Wasserbad nehmen und mit der Maschine aufschlagen.
Gesiebte Mehl-Kakao-Mischung vorsichtig unterheben und im Ofen bei 160 Grad etwa eine halbe Stunde backen.

Fingertest: der Bisquit ist fertig wenn der Fingerabdruck verschwindet.
""").notiz("Für Schokobisquit 30g Kakao und 170g Zucker verwenden.").notiz("Für große Form 6 Eier nehmen, für kleine Form reichen 4 Eier.")

b.add(bisquit)


print(b)
