# list using for loop

lst = []

for i in range(1,11):
    lst.append(i)

print(lst) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Comprehension list

comp_list = [i for i in range(1,11)] # we dont need to put len() inside range(). because we dont iterate throuh
print(comp_list)

comp_list2 = [i /2 for i in range(1,11)]
print(comp_list2) #[0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0] divid 2

comp_list3 = [i * j for i in range(1,11) for j in range(5)] # it means double loop over. i will loop over 5 times.

# TUPLES
comp_tuple = tuple([i for i in range(1,11)])
print(comp_tuple) #(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# set()
comp_set ={i for i in range(1,11)}
print(comp_set)

# dict

comp_dict = {j :i for i in range(1,11) for j in range(5)}
print(comp_dict) # {0: 10, 1: 10, 2: 10, 3: 10, 4: 10}

# how to assign multiple variables

x = y = 1
print(x,y) # both are 1

s, k = 2,3
print(s,k) # s =2,k =3


# Doc Strings document string for someone read your code, comment is very kind and useful.

def foo():
    """
    this is the foo function
    """
    pass

# help

# help(1) # you can read all of documentations

help(max) # 











