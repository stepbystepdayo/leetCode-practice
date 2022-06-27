"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


"""

# This is the solution using Hashmap!
# 1. make hashmap
# 2. loop over the nums and we want to return the index so we need to use enumerate
# 3. make a complemet that target - num
# 4. if num is not in hashmap, make hashmap table
# 5. if there is num in hashmap, return num's index and num's index in hasmap

# from _typeshed import SupportsRead


def solution(nums, target):

    
    # hashmap = {}
    # for index, num in enumerate(nums):
    #     comp = target - num
    #     if num not in hashmap:
    #         print(hashmap)
    #         hashmap[comp] = num, index
    #     else:
    #         return [hashmap[num][1], index]
    # return -1



# This is the solution using two pointers
# 1. we need to sort the nums 
# 2. set up start = [0] and end = [len(nums):-1]
# 3. while loop over start to end 
# 4. we need to make the valiable adding start and end


    
    # need to enumerate nums then, you can see (index, nums)
    nums = enumerate(nums)
    # need to sort each nums not index.
    nums = sorted(nums, key = lambda nums:nums[1])
    print(nums)
    start = 0
    end = len(nums) -1
    # print(start,end) 


    while start < end:
        
        startandEnd = nums[start][1] + nums[end][1]
        # print(startandEnd)
        #if target is less than startandEnd, end will move to left.
        if startandEnd > target:
            end -= 1
        # if target is bigger than startandEnd, start will move to right.
        if startandEnd < target:
            start += 1
        #if target is same number as target, return number of start and end!
        if startandEnd == target:
            # return only index of nums 
            return [nums[start][0],nums[end][0]] 
    return -1





print(solution([2,7,11,15],9)) #[0,1]
print(solution([3,2,4],6))#[1,2]
print(solution([3,3],6)) #[0,1]