#!?usr/bin/env python3

##########################################################################
#Calculating Fibonacci numbers
#This is a famous mathematics series.
#
# 1 1 2 3 5 8 13 21 34
#
#This first two numbers in the series are 1.
#The third number is assigned the sum of the previous two numbers.
############################################################################


###########################################################################
#The traditional way to program the Fibonacci series
###########################################################################
def trad_fib(n):
    a = 1 #The first number in the series
    b = 1 #The second number in the series

    while b < n:
        print(a, end="")
        old_b = b  #Keep the original value of b
        b = a + b  #The new value of b
        a = old_b  #The new value of a
    print(a, end="")
    print()
    return a


#Call the function, to display the Fibonacci numbers less than 400
x = trad_fib(400)
print("The Fibonacci number that is less than 400...",x)

print()

#Call the function, to display the Fibonaci numbers less than 2000
x = trad_fib(2000)
print("The Fibonacci numbers that is less than 2000...",x)
