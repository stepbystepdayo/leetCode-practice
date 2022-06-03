
'''
x = set()
y = {}

print(x) -> <class 'set'>
print(y) -> <class 'dict'>

y = {1,2} -> <class 'set'>
'''

from re import X


# x = {1,2,2,1,2,1}

# x.add(3) # we cannot use append for set {1,2,3}. we can not put other {set}. you can not put any mutable stuffs like [], {} but you can put () tuples!!

# x.remove(2) # remove 2 {1,3}
# x.clear() # it will be set()

# print(len(x)) # 2 {1,2} 
# print(x)
# contain = 1 in x
# print(contain) # True

# s = {1,2}
# k = {2,3}

# z = s.union(k) # you can combine s and k
# c = s | k # | is the same as union(), but you can use only set(). union() shortcut.
# print(z)
# print(c)

# i =  {1,3,4}
# m = {1,3,5}

# y = i.intersection(m) # correcting the same numbers from 2 set().
# t = i & m # this is intersection()'s shortcut

# print(y)
# print(t)

# d = i.difference(m) # 3 
# print(d)

# di = i - m # 3
# print(di)

# # compare to both then, return difference numbers
# dif = i.symmetric_difference(m)

# print(dif) # {4,5}

# dif2 = i ^ m # this is short cut, will give new set

# print(dif2)

# i =  {1,2,3}
# m = {1,2,4}

# i.update(m) # i will modify but m doesn't modify
# m.update(i) # same as above 



# i.difference_update(m)

# print(i)
# print(m)

# x = {1,2,3}
# y = {1,2,3,4,5,6,7}

# print(x.issubset(y)) # True because, inside y there is x value. 
# print(x <= y) # issubset() shortcut
# print(x.issuperset(y)) 
# print(y >= x) # issuperset() shortcut

# # prep issubset() is at least one element inside the other set()

# print(x < y)


x = [1,2,2,2,2,3,4,5,3,4]

set_x = list(set(x))

print(set_x)

numbers =set()

while True:
    num = int(input("Number: "))

    if num in numbers:
        break

    numbers.add(num)

    











