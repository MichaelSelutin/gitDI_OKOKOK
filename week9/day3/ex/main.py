

class Character:
	def __init__(self, name, basic_attack, life = 20, attack = 10):
		self.name = name
		self.life = life
		self.attack = attack

	def basic_attack(self, other):
		other.life -= self.attack

		@staticmethod
		def turn_results(char1, char2):
			print(f"Result:/n/t{char1.name}´s life - {char1.life}/n/t{char2.name}´s life - {char2.life}")


class Druid(Character):
	def __init__(self, name, life=20, attack=10):
		super().__init__(name, life, attack)
		print(f"I am {self.name}, the great druid!")

	def meditate(self):
		self.attack -= 2
		self.life += 5
		print(f"{self.name} meditates. His life rises to {self.life} and attack power goes {self.attack}.")

	def animal_help(self):
		self.attack += 5
		print(f"{self.name} calls his animal, his attack rises to {self.attack}.")

	def fight(self, other_character):
		other_character.life -= 0.75 * (self.attack + self.life)
		print(f"{self.name} attacks {other_character.name}")
		Character.turn_results(self, other_character)


class Warrior(Character):
	def __init__(self, name, life=20, attack=10):
		super().__init__(name, life, attack)
		print(f"I Yield to none!")

	def brawl(self, other_character):
		other_character.life -= 2
		self.life += 0.5
		print(f"{self.name} brawls with {other_character.name}")
		Character.turn_results(self, other_character)

	def train(self, other_character):
		self.life += 2
		self.attack += 2
		print(f"{self.name} trains and gains {self.life} life and {self.attack} attack power.")

	def roar(self, other_character):
		other_character.attack -= 3
		print(f"{self.name} roars and {other_character.name}´s attack decreases to {other_character.attack}.")


class Mage(Character):
	def __init__(self, name, life=20, attack=10):
		super().__init__(name, life, attack)
		print(f"I am alive!")

	def curse(self, other_character):
		other_character.attack -= 2
		print(f"{self.name} curses {other_character.name} and his attack power falls to {other_character.attack}")

	def summon(self):
		self.attack += 3
		print(f"{self.name} summons a helper and his attack power rises to {self.attack}")

	def cast_spell(self, other_character):
		other_character.life -= self.attack / self.life
		print(f"{self.name} casts a spell on {other_character.name} and he loses {other_character.life} life points.")
		Character.turn_results(self, other_character)

war1 = Warrior("He-man")

druid1 = Druid("Yo")

mage1 = Mage("Dodo")

