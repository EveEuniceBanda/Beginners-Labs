#!/usr/bin/env python3

#Initialize two Set objects, using curly brackets
chicago_zoo_set = {'Kangaroo', 'Leopard', 'Moose', 'Polar Bear', 'Bobcat'}
sandiego_zoo_set = {'Lion','Kangaroo', 'Grizzly Bear', 'Wildcat', 'Antelope'}

print()
print("SET OBJECTS...")
print('Chicago Zoo:',chicago_zoo_set)
print('San Diego Zoo:',sandiego_zoo_set)
print()

print("COMMON animals to both the Chicago and San Diego Zoo")
print("Intersection of Chicago and San Diego Zoo")
print(chicago_zoo_set.intersection(sandiego_zoo_set))
#Only Kangaroo

print()
print("UNIQUE animals at the Chicago Zoo")
print("These are items at the Chicago Zoo, but NOT at the San Diego Zoo")
print(chicago_zoo_set.difference(sandiego_zoo_set))
#Should incluee: Leopard, Moose, Polar Bear, Bobcat
#NOTE:It might be printed in a different order

print()
print("UNIQUE animals at the San Diego Zoo")
print("These are items at the San Diego Zoo, but NOT at the Chicago Zoo")
print(sandiego_zoo_set.difference(chicago_zoo_set))
#Should incluee: Lion, Grizzly Bear, Wildcat, Antelope
#NOTE:It might be printed in a different order