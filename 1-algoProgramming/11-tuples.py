x = (1,2,3)
print(x[0]) # 1
# you cannot modify inside of tuples because immutable.

print(len(x)) # 3

count = x.count(1) # 1
idx= x.index(2) #2
contains = 2 in x # True | 4 in x -> Flase

xs = (1,2,3,(1,2),True,[])

print(xs[3]) # (1,2)
print(xs[3][0]) # 1

s = (1,2)
y=(2,4)

combined = s + y # (1,2,3,4)
combined2 = [1,2] * 2 # [1,2,1,2]

num = (1, )

print(x[0]) # 1
print(x[1]) # ERROR beccause there is no element 

ig = (1,2,3)
n = (x[0], 4,x[2])

# if you want to change the tuples, you need to make other variables like n.
print(n) # (1,4,3)
