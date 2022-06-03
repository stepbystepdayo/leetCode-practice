
# for i in range(10):
#     print(i) #0 1 2 3 4 5 6 7 8 9  start from 0
    

# for i in range(3,20): # ->(start,end)
#     print(i) #3,4,5,6,7,8,,,,,19

# for i in range(2,10,2): #-> (start,end,skip)
#     print(i)#2,4,6,8


# for i in range(10, -20, -5):
#     print(i) # 10,5,0,-5,-10,-15


# range(len()) V.S. for loop list V.S. enumerate

# lst =[1,2,3,4,5,True]
# result = 0
# for i in range(len(lst)):
#     print(lst[i])

# when you iterator the list, use rang(len(list))!! then, you can loop over the list!also you can get index!


# for element in lst:
    # print(element)
# you can iterator the list, but you cannot get index.

# for i,element in enumerate(lst):
    # print(i, element)
# you can get index 

# tup = (2,3,4,"hello","tim",True)

# for i in range(len(tup)):
#     element = tup[i]
#     print(element)

# for element in tup:
#     print(element)

# for i, element in enumerate(tup):
#     print(i,element)

# str = "my string"

# for i in range(len(str)):
#     print(str[i])

# lst = [1,2,3,3,4,4,2,1,2]

# for num in lst:
#     if num == 4:
#         break # stop for loop

#     print(num)
# print("DONE")

# for num in lst:
#     if num == 4:
#         continue # stop 4 and continue to after 4

#     print(num)
# print("DONE")



# nested for loop!!!!

#loop over first loop, then second loop will loop over 10, then, first loop will loop 2, then, second loop over 10 times. so total: 10 times loop over

# for i in range(10): # i = 0
#     for j in range(10): #j =0 
#         print(j)


# nested list

# lst = [[1,2],[3,4],[5,6],[7,8]]

# for i in range(len(lst)):
#     new_list = lst[i]
#     print(new_list)
#     for j in range(len(new_list)):
#         print(new_list[j])


# string = "hello world"

# for i,char in range(len(string)):
#     if char == "w":
#         print(i)

# numbers = [] # it can not be inside of loop, because every loop over it will set and be empty , so it doesn't work
# for i in range(10):
#     num = input("Enter a number: ")
#     numbers.append(num)
# print(numbers)

# # pass -> move on the next step. noting is gonna happend

# # for else!!!
# words = ("hello","name","this","is","word")
# target = "name"
# found = False
# for word in words:
#     if word == target:
#         print("I found the world")
#         found = True
# if not found:
#         print("I didn't find the world")


num = int(input("Number "))

for i in range(20,num,-1):
    print(i)

