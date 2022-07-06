'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

'''

# def solution(nums):
#     hashmap = {}

#     for num in nums:
#         if num not in hashmap:
#             hashmap[num] = 1
#         else:
#             hashmap[num] += 1
    
#     print(f"this is hashmap: {hashmap}")

#     for v in hashmap.values():
#         print(f"this is value: {v}")
#         if v > 1:
#             return True
#     return False


# def solution(nums):
#     setMap = set()

#     for num in nums:
#         if num not in setMap:
#             setMap.add(num)
#         else:
#             return True
#     return False


def solution(nums):
    hashmap = {}

    for num in nums:
        if num not in hashmap:
            hashmap[num] = 1
        else:
            return True
    return False



print(solution([1,2,3,1])) # True
print(solution([1,2,3,4])) # False
print(solution([1,1,1,3,3,4,3,2,4,2])) # True
print(solution([2,14,18,22,22])) # True