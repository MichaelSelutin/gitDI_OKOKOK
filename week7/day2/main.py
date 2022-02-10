
#ex1
def display_message():
	print("learning stuff")

display_message()


#ex2

def favorite_book(title):
	print(f"One of my favorite books is {title}")

favorite_book("sherlock")

#ex3

def describe_city(city, country = "Germany"):
	print( city + " is in Germany")

describe_city("hannover")


#ex4

def num():
	user_num = input("Give me a number between 1 and 100 ")
	import random
	ran = random.randint(0, 100)
	if user_num == ran:
		print("Great!")
	else:
		print("Failed! The numbers were: ")
		print(ran, user_num)

num()


#ex5

