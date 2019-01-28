#!/usr/bin/env python3

#################################################################################
#a-list is the ORGINAL LIST
#b_list is a similiar list, with differemt order
#################################################################################
a_list = [1,2,3,4]
b_list = [1,2,3,4]

print("List A: ", a_list)
print("List B: ", b_list)
print()

#################################################################################
#Show that the LIST Order matters
#a_list is NOT EQUAL to b_list
#################################################################################
if(a_list !=b_list):
    print("a_list is NOT EQUAL to b_list.")

#################################################################################
#Modify LIST a_list
#Add the item 5 to the end of the list
#add the itme 6 to the end of the list
#################################################################################
a_list. append(5)
a_list. append(6)

print("After appending items 5 and 6...")
print("a_list: ",a_list)
print()
#This line would fail, becuase append takes only 1 argument
#a_list. append(7,8)

#This line runs, because a list is considered 1 argument
#This will append a 2nd list into the original list
c_list = [7,8,9,10]
a_list.append(c_list)
print()
print("After appending the c_list to the a_list.")
print("a_list: ", a_list)
print()

d_list = [11,12,13,14]
a_list.extend(d_list)

print("After extending the d_list to the a_list:")
print("a_list: ", a_list)




