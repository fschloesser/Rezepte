
from templates import *
from unit import *
from food import *
from book import *


b = book()

alfajores = rezept("Alfajores", "für etwa 20")
alfajores.add(75, margarine).add(50, puderzucker).add(50, mehl).add(175, speisestaerke).add(0.5, backpulver).add(1, ei)

alfajores.schritt(
        """Margarine mit Puderzucker verrühren.
Das Ei hinzufügen und verrühren.
Mehl, Speisestärke, Backpulver dazu mischen, im Kühlschrank ruhen lassen.

Ausrollen und ausstechen.

10-12 Minuten bei 160-180 Grad backen.

Mit Marmelade/Manjar/Schokolade zu Doppelkeksen zusammenkleben.""").notiz(
        "Etwas Mehl kann durch Backakao ersetzt werden.")

b.add(alfajores)


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
