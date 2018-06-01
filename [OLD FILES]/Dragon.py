import random

class Dragon:
	name = ""
	strength = 0
	defense = 0
	health = 0

	def __init__(self,name):
		self.name = name
		self.strength = random.randint(10,20)
		self.defense = 0
		self.health = random.randint(100,200)

	def isalive(self):
		return self.health > 0
