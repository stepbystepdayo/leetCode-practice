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
    setNum = set(arr)
    count = 0
    print(len(setNum))
        
    for num in arr:
        if num not in hashmap:
            hashmap[num] = 1
            count += 1
        else:
            hashmap[num] += 1
            print(hashmap,count)  
        
    for v in hashmap.values():
        print("this is value",v)
        if v == count:
            return True
    return False