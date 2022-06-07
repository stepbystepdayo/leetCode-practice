
# def print_value(value):
#     print(value)

# print_value("hello") 
# print_value(1) 
# print_value(True) 

# def add_5(x,y,z):
#     result = x + y + z + 5
#     print(result)

# x = 4
# y = 5
# z = 6
# add_5(x,y,z)


# def add_5(x,y,z):
#     result = x + y + z + 5
#     return result
#     # if you put something like print("hi") after return, it won't show. return is end of code

# x = 4
# y = 5
# z = 6
# r = add_5(x,y,z)
# print(r)


# def solution(x,y,z):
#     result = x + y + z
#     if result < 0:
#         return result
#     else:
#         return 1

# x = 4
# y = 5
# z = -100
# s = solution(x,y,z)
# print(s)

# defalt prameter!!!!
'''
range(start,end,step)
we can decide the number of start, end and stop in parameter! 
'''

# def new_range(stop, start = 0):
#     x = start

#     while x < stop:
#         print(x)
#         x += 1

# new_range(1,2) 

# new_range(1, start = -5)  we can NOT do this!
# when you want to defalt start = 0, and you just want to put number of stop, you need to write stop first and make defalt of start = 0. 

# you can return multiple values

# def return_value(x,y):
#     return x + 1, y +1 # this will be tuple

# result = return_value(1,2) 
# print(result)


# REMOVE CHARACTORS

# def remove_chars(base, chars):
#     new_string = base
#     for char in chars:
#         new_string = new_string.replace(char,"")

#     return new_string

# result = remove_chars("hello world","l")
# print(result)

# # SUM of both strings

# def sum(lst1, lst2):
#     sum1 = sum_list(lst1)
#     sum2 = sum_list(lst2)

#     return sum1 , sum2

# def sum_list(lst):
#     total = 0

#     for num in lst:
#         total += num
    
#     return total


# print(sum([1,2,3,4],[2,3,4,5]))


# # NESTED FUNCTION!!!

# def sum(lst1, lst2):
#     # we can nest def but, you need to be careful the space!
#     def sum_list(lst):
#         total = 0   
#         for num in lst:
#             total += num

#         return total
#     sum1 = sum_list(lst1)
#     sum2 = sum_list(lst2)

#     return sum1 , sum2




# print(sum([1,2,3,4],[2,3,4,5]))


def running_sums(numbers):
    # Write your code here.
    sumNum = 0
    output = []
    for idx in range(len(numbers)):
        # print(idx)
        sumNum += numbers[idx] 
        output.append(sumNum)
    return output 
    # print(output)

print(running_sums([5,4,2,1,5,6,4]))








