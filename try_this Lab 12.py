#!/usr/bin/env python3

#Global promptFunction get_user_age


#Function name: get_user_age
def get_user_age():
    # Initialize your prompt string
    prompt_age_msg = "Please enter your age"

    #############################################################
    # The prompt strng has been changed to a GLOLBAL variablle
    # Prompt the user for their age
    #...Because the input function returns a string value
    #...We are converting the string valaue to an integer value
    #############################################################
    user_str= input(prompt_age_msg)

    # The string function isdigit returns TRUE if all digits are numeric
    if (user_str.isdigit()):
        user_age = int(user_str)
    else:
        #if they entered a string value, then set the age to 0
        #This will eventurally flag our error condition
        user_age = 0

    # Retuns the user's age
    return user_age

#################################################################################
#BEGIN the main program
################################################################################

#Call the function, get_user_age
my_user_age = get_user_age()

################################################################################
#ERROR CHECKING: Check that the user_age is over 0
################################################################################
while (my_user_age <=0):
    my_user_age = get_user_age()
#END of the while loop, for the USER-AGE intilixation

################################################################################
#Print out a statement using the user_age_variable
################################################################################
prompt_sge_mdg = "wrong format entered, Enter an integer value for your age."
print("Your age is: ", my_user_age, "years old.")
print()
