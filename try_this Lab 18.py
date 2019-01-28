#!/usr/bin/env python3

####################################################
# FUNCTIOPN NAME: mapMe()
#inputs: None
#Retunfs a tuple contiaining GPS coordinates of Latitude and Longitude
##########################################################################
def mapMe():
    #This is Geo-Coordinates for Chicago
    latitude = ('41.881832 degrees North')
    longitude = ('87.6298 degrees West')

    #Line 15 works because Python packs it into a tuple
    #Line 16 also works, because you are retruning it in a tuple
    #return latitude longitude
    #retrun(latitude, longitude)

    #Line 19 works becuase it is a list! It is also considered 'one thins'!
    return [latitude, longitude]


print('The geo-ciirdubates fir Chicagp are:')
myLocation = mapMe() # Here, we are assigning the retrun valaue of the function mapMe to myLocation

print("What does mapMe return??? A list or a tuple?")
print("... A list is formateed with square brackets [1,2,3]")
print("... A tuple is formateed with parantheses (1,2,3")

print("Mylocation is:", myLocation)
print("")

print('My Latitude is: ' + str(myLocation[0]))
print('My Longitude is: ' + str(myLocation[1]))





