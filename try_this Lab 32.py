#!/usr/bin/env python3

#Here are some very large numbers!!!!
num1 = 10 **40
num2 = 10 ** 40 + 1

print("Python supports really large numbers!")
print()

print("num1 is 10 raised to the 40th power")
print("num2 is num1.plus 1")
print()
print("num1 is: ", num1)
print("num2 is: ", num2)

print()
print("How precise are these large numbers???")
print("...Now testing if num1 is less than mum2")
my_boolean = (num1 < num2)
print(my_boolean)

print()
print("... Now testing if num1 is equal to num2")
my_boolean = (num1 == num2)
print(my_boolean)
print()

###########################################################
#A googol* is 10 raised to the 100th power
###########################################################
print("What is a googol????? num3 is a googol. See belwo.")
print("num3 is 10 raised to the 100th power")
print("num4 is num3,plus 1")
num3 = 10 ** 100
num4 = 10 ** 100 + 1

print("num3 is: ", num3)
print("num3 is: ", num4)

print()
print("...Now testing if num4 is larger than num3")
my_boolean = (num4 > num3)
print(my_boolean)













