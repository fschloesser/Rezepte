
from templates import *
from unit import *
from food import *


class ingredient:

    def __init__(self, quantity, food):
        self.quantity = quantity
        self.food = food

    def __str__(self):
        return str(self.food)

    def cals(self):
        return self.food.cals * self.quantity

    def get_tableline(self):
        return temp_tableline.format(
                quantity=self.quantity,
                unit=self.food.unit,
                food=self.food.name
                )


class rezept:

    def __init__(self, title, subtitle):
        self.title = title
        self.subtitle = subtitle
        self.spacing = self.space()
        self.steps = []
        self.ingredients = []
        self.notes = []

    def __str__(self):
        if len(self.ingredients) == 0 or len(self.steps) == 0:
            return ""
        return temp_recipe.format(
                title=self.title,
                spacing=self.spacing,
                cals=self.cals(),
                subtitle=self.subtitle,
                ingredients=self.get_ingredients(),
                instructions=self.get_instructions())

    def space(self):
        return 20

    def cals(self):
        return sum([i.cals() for i in self.ingredients])

    def get_ingredients(self):
        if len(self.ingredients) == 0:
            print("something is wrong in recipe.get_ingredients")
            exit(0)
        return newline.join([i.get_tableline() for i in self.ingredients])

    def get_instructions(self):
        return paragraph.join(self.steps + ["Notiz: {n}".format(n=n) for n in self.notes])

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
        return "Book:{p}{b}".format(p=paragraph, b=paragraph.join([str(r) for r in self.recipes]))

    def add(self, rec):
        self.recipes.append(rec)


b = book()

bisquit = rezept("Bisquit", "sehr fluffy, gut zu schneiden, 1655 kcal")
bisquit.add(6, eier).add(150, zucker).add(90, mehl).add(30, maismehl)

bisquit.schritt(
        """Eier und Zucker über einem Wasserbad vermischen bis der Zucker sich aufgelöst hat, das Ei soll nicht stocken.
Vom Wasserbad nehmen und mit der Maschine aufschlagen.
Gesiebte Mehl-Kakao-Mischung vorsichtig unterheben und im Ofen bei 160 Grad etwa eine halbe Stunde backen.""").schritt(
        "Fingertest: der Bisquit ist fertig wenn der Fingerabdruck verschwindet.").notiz(
        "Für Schokobisquit 30g Kakao und 170g Zucker verwenden.").notiz(
        "Für große Form 6 Eier nehmen, für kleine Form reichen 4 Eier.")

b.add(bisquit)

print(str(b))

print(globals())
