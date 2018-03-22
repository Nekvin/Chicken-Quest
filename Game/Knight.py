from random import Random

class Warrior:
	name = ""
	strength = 0
	defense = 0
	health = 0
	
	def __init__(self, name):
		self.name = name
		zufall = Random()
		self.strength = 10
		self.defense = 20
		self.health = 50 + self.defense

	def isalive(self):
		return self.health > 0
