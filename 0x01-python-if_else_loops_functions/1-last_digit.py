#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = number % 10 if number > 0 else int(repr(number)[-1]) * -1
if x < 6:
       print("Last digit of {:d} is {:d} and is less then 6 and not 0".format(number, x))
elif x > 5:
       print("Last digit of {:d} is {:d} ans is greater than 5".format(number, x))
else:
       print("Last digit of {:d} is 0 and is 0".format(number))
