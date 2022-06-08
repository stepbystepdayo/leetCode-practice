
'''
[1,2,3,4,5]
object : Integr
type:list

IMMUTABLE:
int   x = 1 when we change 1, we need to make other variable to change 
float
str
tuple
bool

MUTABLE:
list
set()
dict

'''
# list example: 
# x = []

# def func(lst,x):
#     lst.append(x)
#     print(lst)

# a = []
# func(a,2) #[2]
# func(a,3) # [2,3] list is changeable 
# print(a)

# dictionary example:

# d = {}
# d["k"] = "v"

# a = d
# a["a"] = "b"

# print(d,a)

#set example:

s1 =set()
s2 =s1

s1.add(1)
s2.add(2)

print(s1 is s2) # True

def func(s,x):
    s.add(x)

s1 =set()
func(s1,1)
print(s1)

a = [1,2,3]
b = a[:] # this is meaning of blandnew object(copy of object)

print(a is b) # False

def func(lst):
    lst = lst[:] # copy of object
    lst.append(4)

x = [1,2,3]
func(x)
print(x) # [1,2,3] it wont change because, you made copy of lst. 


s1 ={1,2,3}
s2 =s1.copy() # copy() will made a different object(copy of object)

s1.add(4)
print(s1,s2)


lst =[[1,2,3],[3,4,5]]

lst[0].append(4)
lst[1].append(4)

print(lst)

lst =[1,2,3]
d = {1:lst}

lst.append(4) 
print(d) # {1:[1,2,3,4]}


a = [1,2]
b =[3,4]
tup = (a,b)

a.append(1)

print(tup) 

a = [[1,2,3]]
b =a[:]

c = a[0]
c.append(4)


