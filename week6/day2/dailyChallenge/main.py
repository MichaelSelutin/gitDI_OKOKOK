

password = input("Please write a string of 10 chars ")

if len(password) < 10:
    print("string not long enough")
elif len(password) > 10:
    print("string loo long")

print(password[0])
print(password[0:2])
print(password[0:3])
print(password[0:4])
print(password[0:5])
print(password[0:6])
print(password[0:7])
print(password[0:8])
print(password[0:9])
print(password[0:10])

arr = password.split(' ')

import random
random.shuffle(arr)

print(arr)