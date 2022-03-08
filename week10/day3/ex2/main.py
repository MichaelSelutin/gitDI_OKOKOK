#ex1
import datetime

# x = datetime.datetime.now()
# print(x)


#ex2


# x = datetime.datetime(2023, 1, 1)
#
# y = datetime.datetime.now()
#
# z = x - y
#
# print(f"the 1st of january is in {z} and hours")

#ex3
from datetime import date

def calculateAge(birthDate):
	today = date.today()
	age = today.year - birthDate.year
	((today.month, today.day) <
	 (birthDate.month, birthDate.day))
	return age

# Driver code
print(calculateAge(date(1997, 2, 3)), "years")

