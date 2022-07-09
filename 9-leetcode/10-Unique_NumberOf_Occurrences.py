'''
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true


'''

def solution(arr):
    hashmap = {}
    checkV = set()

    # need to make hashmap
    for num in arr:
        if num not in hashmap:
            hashmap[num] = 1
        else:
            hashmap[num] += 1

    # need to loop over values of hashmap
    for v in hashmap.values():
        if v in checkV:
            return False
        else:
            checkV.add(v)
    return True


print(solution([1,2,2,1,1,3])) # True
print(solution([-1,-1,-1,-3,-1,-1])) # True
print(solution([1,2])) # False
print(solution([-3,0,1,-3,1,1,1,-3,10,0])) #True
