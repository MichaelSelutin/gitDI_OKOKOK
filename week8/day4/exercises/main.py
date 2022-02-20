
#ex1
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Persian(Cat):
	def sing(self, sounds):
		return f'{sounds}'

class Garfield(Cat):
	def sing(self, sounds):
		return f'{sounds}'

class BlueCat(Cat):
	def sing(self, sounds):
		return f'{sounds}'

my_cats = []

my_cats.append(Cat("Bengal", 3))
my_cats.append(Cat("Chartreux", 4))
my_cats.append(Cat("Persian", 8))
my_cats.append(Cat("Garfield", 6))
my_cats.append(Cat("BlueCat", 44))

for obj in my_cats:
	print(obj.name)


#ex2

class Dog():
	def __init__(self, name, age, weight):
		self.name = name
		self.age = age
		self.weight = weight

	def bark(self):
		for dog_name in self.name:
			print(dog_name.name("f{dog_name} is barking"))

print(Dog("yo", 22, 5))
