# Dictionary is a special DS where you can create your own customize indexes
# it is mutable too and sequential

my_Dict = { 
    "name":"Ingenuity Gaming",
    "location":"sector-144",
    "count":500,
    5:"new Index system"
    }

print(my_Dict["name"])
print(my_Dict[5])

print(my_Dict.items())
print(my_Dict.keys())
print(my_Dict.values())


for i,j in my_Dict.items():
    print(i,"-" ,j)