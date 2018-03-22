from random import Random
from Knight import Knight
from Dragon import Dragon

def berichteKampf(attacker, defender):
	print(defender.anzeigen(), "wird angegriffen von")
	print(attacker.anzeigen(), "mit Stärke",
			attacker.gibStärke(), "und verteitigt sich mit",
			defender.armor)
	print("****")

zufall = Random()
arthur = Knight("Arthur")
wilhelm = Dragon("Drogk")

print(arthur.anzeigen(), "vs", wilhelm.anzeigen(), "\n")

while arthur.istAmLeben() and wilhelm.istAmLeben():
	if bool(zufall.choice([True, False])):
		berichteKampf(arthur, wilhelm)
		arthur.angreifen(wilhelm)
	else:
		berichteKampf(wilhelm, arthur)
		wilhelm.angreifen(arthur)

if arthur.istAmLeben() == True:
	gewinner = arthur
else:
	gewinner = wilhelm

print("\nGewonnen hat:", gewinner.anzeigen())
