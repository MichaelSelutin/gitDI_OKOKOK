#ex1

# my_fav_numbers = {2, 3}
#
# my_fav_numbers.remove(3)
#
# print(my_fav_numbers)
#
# friend_fav_numbers = {8, 9, 5}
#
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
#
# print(our_fav_numbers)


#ex2

#no, you can add anything to a tuple

#ex3

# x = range(1, 21)
# for n in x:
# 	print(n)


#ex4

#integer is a full number, float with a dot.

# sequence = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
#
# print(sequence)


#ex5

# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
#
# basket.remove("Banana")
#
# basket.remove("Blueberries")
#
# basket.append("Kiwi")
#
# basket.append("Apples")
#
# count = basket.count("Apples")
#
# print(count)
#
# basket.clear()
#
# print(basket)


#ex6

# username = input("What is your name? ")
#
# while username != "Michael":
# 	username = input("try again ")
# 	continue
# else:
# 	print("Best name ever!")


#ex7

list1 = [10, 21, 4, 45, 66, 93]

for num in list1:

	# checking condition
	if num % 2 == 0:
		print(num, end=" ")