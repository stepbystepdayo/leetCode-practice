'''
x = 0
while x < 5:
    print(x)
    x += 1   
    
for i in range(5):
    print(x)

# when you know how many for loop you need to do, you should use for loop because, you can just enter that number many times!
# However, if you dont know how many loop over should we do, use while loop.

'''



num = input("Enter an integer: ")

while not num.isdigit():
    num = input("Enter an integer: ")

# while loop just keep going. it never break the loop. so it will crush. 



while True:
    num = input("Enter an integer ")
    if num.isdigit():
        break


lst = [2,3,3,2,2,1]

result = 0
i = 0

while result < 9:
    num = lst[i]
    result += num
    i += 1
    print(num)




lst = [2,3,3,-2,-2,-1]
# if inside array, there is negative value like -2,-2,-1, it will crush because, they can not do += 1. 
# so we need to put i < len(lst) inside while loop.

result = 0
i = 0

while result < 9 and i < len(lst):
    num = lst[i]
    result += num
    i += 1
    print(num)


# if you found specific value, how to stop the while loop.

lst = [2,3,3,-2,-2,-1]
i = 0

while i < len(lst):
    if lst[i] == -2:
        print("yayy found it")
        break
    i += 1
    # if there is not i += 1, it will continue forever. dont forget it.
    else:
        print("didn't find it")