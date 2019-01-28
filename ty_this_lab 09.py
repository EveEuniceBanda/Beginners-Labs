#!//usr/bin/env python 3

# ASCII character are used to represent letters, puncuation, numbers

#Python actually usses Unicode, which is nummeric

print("The ORD function...")
############################################################################################
#ORD function
#To get a numeric code for a character, use the Python ord function
############################################################################################
#Loop through this character string
#This will convert each character in this string to a numeric value
for myChar in 'abcdefgh':
    myNum = ord(myChar)
    print(myChar, myNum)


print()
print("The CHR function...")

##############################################################################################
#Char function
#Here you can loop through a ASCII numeric code back to a characteer form
#To get a character from a numeric code, use the Python chr function.
##############################################################################################
#Loop through the integers 65-74
#Convert each integer to its character form
for i in range(65, 75):
    myChar = chr(i)
    print(i, myChar)


print()
print("The HEX function...")
################################################################################################
#HEX function...0x denotes that the value is in hexadecimal format
################################################################################################
#Loop thhough the integers 1-16
for j in range(1, 17):
    myHexValue = hex(j)
    print(j, myHexValue)


