'''
Given an integer n and an array a of length n, your task is to apply the following mutation to a:

Array a mutates into a new array b of length n.
For each i from 0 to n - 1, b[i] = a[i - 1] + a[i] + a[i + 1].
If some element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, it should be set to 0. For example, b[0] should be equal to 0 + a[0] + a[1].
Example

For n = 5 and a = [4, 0, 1, -2, 3], the output should be solution(n, a) = [4, 5, -1, 2, 1].

b[0] = 0 + a[0] + a[1] = 0 + 4 + 0 = 4
b[1] = a[0] + a[1] + a[2] = 4 + 0 + 1 = 5
b[2] = a[1] + a[2] + a[3] = 0 + 1 + (-2) = -1
b[3] = a[2] + a[3] + a[4] = 1 + (-2) + 3 = 2
b[4] = a[3] + a[4] + 0 = (-2) + 3 + 0 = 1
So, the resulting array after the mutation will be [4, 5, -1, 2, 1].

'''

import enum


def solution(n, a):
    # result = []
    # if n == 1:
    #     return a
    # for idx in range(len(a)-1):
    #     if idx == 0:
    #         firstNum = 0 + a[0] + a[1]
    #         # print(firstNum)
    #         result.append(firstNum)
    #     if idx == len(a) -2:
    #         # when you hit len(a)-2 thats mean 2, a[-1]+a[-1]+0. then, already last number was gone by range(len(a)-1) when you did loop over.
    #         lastNum = a[-2] + a[-1] + 0 
    #         # print(lastNum)
    #         result.append(lastNum)
    #     else: 
    #         num = a[idx] + a[idx +1] + a[idx + 2]
    #         # print(num)
    #         result.append(num)
    # return result

    result = []

    for i, number in enumerate(a):
        if i - 1 < 0:
            result.append(0 + a[i] + a[i+1])
        if i + 1 > len(a)-1:
            # when i+1 hit last elements of a, append(a[i] + a[i-1])
            result.append(a[i] + a[i-1])
        else:
            result.append(a[i-1] + a[i] + a[i +1])

    return result

print(solution(5,[4, 0, 1, -2, 3])) #[4, 5, -1, 2, 1]  