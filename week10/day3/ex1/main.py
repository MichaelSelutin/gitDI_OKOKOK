
# ex2
# from random import randint
#
# comp = randint(0, 101)
# print(comp)
# player = int(input("Choose a number between 1 and 100:  "))
#
# if 0 <= player >= 100:
#     print("try again")
# if player == comp:
import string
from random import random

# print("You won")


# ex3
import string
import random

N = 5

res = ''.join(random.choices(string.ascii_uppercase +
                             string.ascii_lowercase, k = N))

print("The generated random string : " + str(res))

