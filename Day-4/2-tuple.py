# Tuple is a data structure with property of Immutable
# It makes your list to be a constant list

my_tuple = (34,22,13,34,45,56,27)
# my_tuple[4] = 50
print(my_tuple)
# print(type(my_tuple))
# my_tuple.add(101)
# print(my_tuple)

for i in my_tuple:
    print(i+1)
# my_tuple.pop()
# print(my_tuple)


temp_list = list(my_tuple)
temp_list.append(100)
my_tuple =tuple(temp_list)
print(my_tuple)