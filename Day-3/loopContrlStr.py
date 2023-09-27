import random
# Loop Control Structure in python
# 1. while
# 2. for loop
# 3. for loop with range (print some serise)


# parts of Loop 
# 1. Initilalization
# 2. condition to stop loop
# 3. Increment | Decrement to  proceed with the loop 

# While Loop
# i = 0
# while(i<=100):
#     i += 1 

#     if(i==45 or i==91):
#         break
#         # continue  
#     else:
#         if(i%2!=0):
#             print(i)
           

# for Loop used for collection [list, set, dictionary]
names =  ["Rahul", "Sachin", "Manish", "Roman", "Himanshu"] 

# for i in names:
#     print(len(i), end=" ")
#     print(i.upper())


# name = "Ingenuity gaming"
# for i in name:
#     print(i.upper())


# # for using range()
# for i in range(2,51,2):
#     print(i)

# for i in range(1,6):
#     print(random.randint(1,100))

# for i in range(1,11):
#     print(i*i, end = " ")

# Generate a matrix of 3x3

for i in range(0,3):
    for j in range(0,3):
        print(random.randint(1,100), end=" ")
    print()    

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for i in adj:
    for j in fruits:
        print(i, " ", j)