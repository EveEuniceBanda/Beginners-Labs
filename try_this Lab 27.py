#!/usr/bin/env python3

s1 = "%to, two, too!"

#######################################################
#strip various characters from the string
#NOTE this aplies to only LEANING and TRAILING charachetrs
#######################################################
s2 = s1.strip('%!') #Strip just the % and ! characters
s3 = s1.strip(",") #Srtip only the comma

print("1:",s1)
print("z2: ", s2)
print("s3:",s3)

s4 = ",,anotherstring,,"
s5 = s4.strip(',')
print("s4: ", s4)
print("s5: ",s5)

s6 =" Leading spaces at beginning and the end   "
s7 = s6.strip('')
print("s6: ",s6)
print("s7: ", s7) #Now here are no leading spaces at the beginning and end












