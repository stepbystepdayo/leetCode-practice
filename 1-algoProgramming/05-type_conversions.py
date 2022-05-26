# Converting

x = "4" 
y = int(x) # can convert to int 4

# print(type(y)) #<class 'int'>
# print(type(x)) #<class 'str'>
# print(type(y)) #<class 'int'>

# print(int("4.5") -4) # ERROR

yx = float("4") + 4  
# print(yx) # 4 float(str) can be int so answer is 8.0


xy = bool("4")
# print(xy) # True | string will be True. even any content inside string will be True.

# ONLY 0 is going to be False!!!!



# s = str("4") + 4 # 44


# number = input("fav num: ")
# result = int(number) + 5 # we need to convert int!! we can not addition string.


# in Python,when a float is converted to int, its decimal part is stripped off! so ans = 9
# ans = int(9.7)
# print(ans)

ans2 = str(bool(x // 2 - 5))
print(ans2)







