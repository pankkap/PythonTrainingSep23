# Set is Data Structure which doesn't allow dupicate data
#set is not sequential DS and not iteratable

# union and intersection 

my_set1 = {1,23,4,5,7,7,8,78,23,1,4,6}
print(my_set1)
print(len(my_set1))
my_set1.add(178)
print(my_set1)
print(len(my_set1))


my_set2 = {23,4,7,78, 10,11,12}
my_set3 = my_set1.union(my_set2)
print(my_set1)
print(my_set2)
print(my_set3)
my_set4 = my_set1.intersection(my_set2)
print(my_set4)
