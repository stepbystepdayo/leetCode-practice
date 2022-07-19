
def solution(nums,target):
    hashmap = {}

    for index, num in enumerate(nums):
        
        comp = target - num
        if comp in hashmap:
            return [hashmap[comp], index]
        hashmap[num] = index
    
    return -1

print(solution([2,7,11,15], 9)) #[0,1]
print(solution([3,2,4], 6))# [1,2]
print(solution([3,3], 6)) #[0,1]


'''
need to know 2 index of the number is substructed from target and the number was substructed.


'''