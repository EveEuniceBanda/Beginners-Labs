#!/usr/bin/env python3

################################################
# a_list is the ORIGINAL LIST
#################################################
a_list = [1,2,3,4]

print("The orginal list...")
print(a_list)
print()
                              #thid simply prints an empty line (more below)
###########################################################################
#Using the FOR loop, with enumerate to navigate the entire list
###########################################################################
#NOTE that i is the index used to access a given item in the list
#This demonstrates that we can chang a valaue in the list
#
#item is a placholder, but it is called anywhere in he program
#item is not a reserved keyword. You could call it "x" if desired.
############################################################################
for i, item in enumerate(a_list):
    a_list[i] = 100       #This changes the value in the list
#END of the FOR Loop

###########################################################################
#Print the modified list
#NOTE that each item should now be 100.
###########################################################################
print(a_list)




