'''
x = {2: "hello", "1":5} 

print(x[2]) # hello x[key] -> it returns value(hello) 

y = {}
x["key"] = "value"
print(y) # {"key":"value"}

s = dict() # it will make dictionary for us

'''

# DELETE dictionaries

# sp = {4:1,2:2,3:3}

# del sp[1] # {2: 2, 3: 3}

# # print(sp)

# # How to check specific keys

# contains = 1 in sp

# print(contains) # True because, there is 1(key) in sp

# values = sp.values()

# print(values) # dict_values([1, 2, 3])

# # this is more specific values. need to put list()
# specificV = list(sp.values())

# print(specificV[0]) # 1

# # GET KEY

# keys = list(sp.keys())

# print(keys[0])

# # ITEMS!! you can get keys and values

# items = list(sp.items())

# print(items) # [(4, 1), (2, 2), (3, 3)] you can get items by tuples



# using for loop

sp = {4:1,2:2,3:3}

# first 
for key in sp:
    value = sp[key]
    print(key, value)
# second
for key, value in sp.items():
    print(key, value)


x = {2:1,3:3,4:1} #-> {2: 1, 3: 3, 4: 2}

x[4] = x.get(4, 0) + 1

print(x)



# how to count the chars 
chracters = {}

string = "hello world"

for char in string:
    chracters[char] = chracters.get(char,0) + 1

print(chracters)

# using while 
counts = {}

while True:
    num = input("Number (enter q to quit): ")

    if num  == "q":
        break
    num = int(num)
    counts[num] = counts.get(num, 0) + 1

print(counts)

# 

d = {"a" : 1, "b" :1,"c":1,"d":1}
l =["a","b","c","d"]












