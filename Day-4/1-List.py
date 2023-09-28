my_list1 = [223,46,8,23,46,3]
          # -6 -5 -4 -3 -2 -1     -ve indexing

print(my_list1)
print(type(my_list1))

my_list2 = ["pankaj", "manish", "nitin", "vikas"]
print(my_list2)

my_list3 = ["name", 1,2,3, True, my_list1]
print(my_list3)
print(len(my_list1))

# iterate a list with while loop
# i = 0
# while(i<len(my_list1)):
#     print(my_list1[i], end=" ")
#     i+=1

# iterate a list with for loop
for i in my_list3:
    print(i, end= " ")

# selective indexing 
print()   
print(my_list1[1:4])
print(my_list1[:-2])

print(my_list1[-2:])
print(my_list1[-1])

# PRINT LIST IN A REVERSE ORDER
print(my_list1[::-1])


# UPDATING DATA IN LIST
my_list2[1] = "Raghav"
print(my_list2)


# Adding new data inti List
my_list3.append("Ingenuity") #adding new data at end of list
print(my_list3)

my_list3.insert(1, "Gaming")
print(my_list3)


#Remmove element from List
my_list3.pop()   #removing last element
print(my_list3)

del my_list3[1]   #removing  element by index
print(my_list3)

my_list2.remove("nitin") 
print(my_list2)


my_list2.clear()  #clear thr entire list of elements
print(my_list2)

del my_list1
print(my_list1)