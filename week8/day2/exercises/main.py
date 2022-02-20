# ex1
class Cat:
	def __init__(self, name, age):
		self.name = name
		self.age = age


c1 = Cat("hopy", 12)

c2 = Cat("Hupy", 90)

c3 = Cat("Happy", 11)


l = c1.age, c2.age, c3.age


oldest = max(l)
print(f"the oldest cat is {oldest}")



#ex2

class Dog:
	def __init__(self, name, height):
		self.name = name
		self.height = height

d1 = Dog("Struppi", 50)
d2 = Dog("Lassi", 22)

def bark(self):
    print("{} goes woof!".format(self.name))

bark(d1)


def jump(self):
    print("{} jumps ".format(self.name) + format(self.height) + " cm high")

jump(d2)

