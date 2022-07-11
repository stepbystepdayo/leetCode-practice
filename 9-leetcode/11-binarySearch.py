'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''

def solution(nums,target):
    start = 0
    end = len(nums)-1

    while start <= end:
        piv = (start + end) // 2

        if nums[piv] == target:
            return piv
        if nums[piv] < target:
            start += 1
        if nums[piv] > target:
            end -= 1
    return -1
    





print(solution([-1,0,3,5,9,12],9)) # 4
print(solution([-1,0,3,5,9,12],2)) #-1
print(solution([5],5)) # 0