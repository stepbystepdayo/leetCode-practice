

def solution(nums,target):
    nums.sort()
    # print(nums)
    start = 0
    end = len(nums) -1

    while start < end:
        comp = nums[start] + nums[end]
        if comp > target:
            end -= 1
        if comp < target:
            start += 1   
        if comp == target:
            return [start, end]
        
    
#　今回の間違え：　compをifステイトメントで比べてなかった。ポインターを動かしてなかった。





print(solution([7,2,11,15],9)) #[0,1]