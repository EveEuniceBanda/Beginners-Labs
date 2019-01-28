#!?usr/bin/env python3
##########################################################################
#Calculating Fibonacci numbers
#This is a famous mathematics series.
#
# 1 1 2 3 5 8 13 21 34
#
#The first two numbers in the series are 1.
#The third number is assigned the sum of the previous two numbers.
############################################################################

###########################################################################
#Note that the function returns the value of a
#This is the last number displayed, as "new a value = b"
#
#If changed to b, then it displays the "new b value, a +b "
###########################################################################
def fib(n):
  a, b = 0,1
  while b < n:
   print(b, end="")
   a, b = b, a+b #see the maaning below!

  print()        #Print an empty line
  return a       #Return the last number displayed

###########################################################################
#MEANING of 'a, b=b, a+b'
##########################################################################
#This does multiple assignments and uses original values!
#...Examine the left side of the assignment operator "="
#...The variable, aand b, will both be given new values
#...a will be assigned to the old value of b
#...b will be assigned to sum of the old values of a+b
###########################################################################
#Call the function, to display the Fibonacci numbers less than 100
x = fib(100)
print("The Fibonacci number that is less than 100...",x)
print()

#Call the functionm to display the Fibonacci numbers less than 500
x = fib(500)
print("The Fibonacci numbers that is less than 500...",x)
print()

#Call the function, to display the Fibonacci numbers less than 2000
x = fib(2000)
print("The Fibonacci)numbers that is less than 2000...",x)


