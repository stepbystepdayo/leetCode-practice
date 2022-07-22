    # MAIN CODE
    # we will use a hashmap to record how many count we have of each letter in array
    # for example, for "[7,3,2,7]" => {7:2, 3:1, 2:1}

    # subsequencyFreq = {}

    # for number in subsequence:
    #     # lets count!
    #     if number not in subsequencyFreq:
    #         subsequencyFreq[number] = 1
    #     else:
    #         subsequencyFreq[number] += 1
    # print(subsequencyFreq)

    # now, let's count down, use the freq map to see if each number in subsequence is in array, in order.

# this is test for abs()
# test= abs(-2.3)
# test2 = abs(3-4j)
# print(test,test2)



# practice for loop over values

# randomObj = {"sayo": 27, "kai": 30, "micah": 25 }

# def loopOverDict(obj):

#     for key in obj:
#         print(f"this is the key, {key}")
#         print(f"Here is the value:{obj[key]}")

        

    
# loopOverDict(randomObj)


# SORTING!!! 
# Insertion Sort and Bubble sort are stable so these are so useful

# Insertion Sort

# def sort_list(unsorted_list):
#     for i, entry in enumerate(unsorted_list):
#         current = i
#         while current > 0 and unsorted_list[current] < unsorted_list[current - 1]:
#             unsorted_list[current], unsorted_list[current -1] = unsorted_list [current -1],unsorted_list[current]
#             current -= 1
#         return unsorted_list

# if __name__ == '__main__':
#     unsorted_list = [int(x) for x in input().split()]
#     res = sort_list(unsorted_list)
#     print(' '.join(map(str, res)))

# Bubble Sort





#lambda Python

# def calc(base, height):
#     return base * height /2

# print(calc(2,5))

# test = (lambda base, height: base * height/2)(5,10)

# print(f"this is lambda test: {test}")

# change all names to capital




# def capital(students):
#     return [student.upper() for student in students]

# print(capital(['Mizoguchi','lovingfoss','TaNaKa','kiBa']))


# # When you use lambda!

# def usingLambda(names):
#     return list(map(lambda name:name.upper(),names))

# print(usingLambda(['Mizoguchi','lovingfoss','TaNaKa','kiBa']))




# def practice(numbers):
#     first = numbers[0]
#     second = numbers[1]
#     count = 0
#     for i in range(len(numbers)-1):
#         if numbers[i] == first:
#             # print(numbers[i])
#             print(f"this matches first, index is {i} and value is {numbers[i]}")
#         elif numbers[i] == second:
#             print(f"this matches second, index is {i} and value is {numbers[i]}")
#         else:
#             count += 1
#     return count

# names = ["kai", "sayo", "micah", "jed", "hirona", "marisa"]

# for i in range(len(names)):
#     print(names[1])
# print(names[1])
# print(practice([4, 3, 2, 3, 2, 5, 4, 3])) # 3

# print(practice([3, 3, 1, 1, 3])) #2


# lst = [[5,6,[100]],[1,2],[1,2,3]]

def solution(lst):
    for i in range(len(lst)):
        print(lst[i][0] *lst[i][1])
        # kake = lst[0] * lst[1]
        # print(kake)


print(solution([[5,6],[1,2],[1,2,3]]))
