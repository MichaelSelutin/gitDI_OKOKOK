



# ex1


print("hello world" * 4)

#ex2

x = (99^3) * 8

print(x)

#ex3

#>>> 5 < 3  #false
#>>> 3 == 3  #true
#>>> 3 == "3"  #true
#>>> "3" > 3  #false
#>>> "Hello" == "hello"  #true


#ex4

computer_brand = "Dell"

print("I have a", computer_brand, "Computer")


#ex5


name = "Michael"
age = 43
shoe_size = 42

info = ("Hi, My Name is", name, "I am", age, "years old. That is one year more than the size of my shoes")
print(info)


#ex6

a = 5
b = 3

if a > b:
    print("Hello world")

#ex7

num = int(input("Give me a number "))
if (num % 2) == 0:
   print("your number is even")
else:
   print("your number is not even")


#ex8

nam = input("What is your name? ")

if nam == "Michael":
    print("Wow, we have the same name!")
else:
    print("Very close, but your name is not good")


#ex9


height = int(input("How tall are you in inches? "))
height_incm = height*2.54

if height_incm > 145:
    print("You can ride the ride")
else:
    print("You need to grow!")