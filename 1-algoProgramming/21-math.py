'''
abs(): 
This is absolute value. remove negative. -9 -> 9

max():
show the maximum number or something
max(1,2) -> 2
max("a","b") -> "b" order's b is greater than "a" 

min():
show the minimun number or something
max(1,-2,-4) -> -4
max("a","b") -> "b" order's b is greater than "a" 

sum():
addition the number. sum() does NOT take multiple value like sum(2,3,4,5). you should iterateble.
sum([2,3,4,5]) -> 14

round():
round(3.45) -> 3
round(3.5) -> 4

round(3.49, 1) ->  3.5
round(3.214,3) -> 3.214
round(3.456566,5) -> 3.45657


'''

# x = round(3.4945,4)
# print(x)

# import math
# # there are bunch of packages in math.

# # sin, cosin, tan 三角関数
# x = math.sin() 
# x = math.cos(math.pi)
# x = math.tan()

import random 
# you can get random numbers

random_number = random.randint(1,10,2)
# random.randint(start,end,step)
print(random_number)
# you can get random number until 1 to 10. 

lst =["he","hi","ho","hello"]
random_char = random.choice(lst)
print(random_char)
# you can get random of string inside list






