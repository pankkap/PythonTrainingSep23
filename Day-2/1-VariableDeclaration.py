# Variable Declaration Rules
# 1. variable names are case sensitive
# 2. variable name should not start from number
# can be alphabet or special character _ (underscore)

name = "Pankaj"
NAME = "Sachin"
print(name)
print(NAME)

first_Name = "Manish"
# 1stname = "manish"
# 3. There should be no space allowed in the variable declaration
firstName = "Manish"

# 4. keyword not allowed as variable name
# break = 5
# in = TRUE

# 5. variable name should follow camel case syntax (Recommendation) 
myLastName = "kapoor"

# snakeCase
first_Name  

# PascalCase
MyLastName = "sdsd"

# Multiple variable declaration
firstName, lastName = "pankaj", "kapoor"
print(firstName)
print(lastName)

# Multiple variable assignment
a=b=c=d=e = 10

# unpacking of data
names = ["pankaj1", "manish2", "sachin"]
cand1,cand2,cand3 = names
print(cand1)
print(cand2)

print(a+b)
# + operator applied to string will concatenate data 
print(firstName+" " +lastName)

print(first_Name,end=" ")
print(myLastName)