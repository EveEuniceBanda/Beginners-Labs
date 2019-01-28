#!/usr/bin/env python3

#Input string that use different characters as delimiters
s1 = "Donald, Victoria, Andrew, Sarah"
s2 = "Donald Victotia Andrew Sarah"
s3 = "Donald@Victoria@Andrew@Sarah"

#print out the initial strings
print("s1: ", s1)
print ("s2: ", s2)
print ("s3: ", s3)

#Split the string, creae a list using a comma-separator
list1 = s1.split(',')
print("list1: ", list1)

#Split the string, create a list using the default space
list2 = s2.split()
print("list2: ", list2)

#Split the string create a list using the @ charachet as a delimiter
list3 = s3.split ('@')
print("liat3: ", list3)














