

# we need to round

def quickRound(nums):
    
    minNum = min(nums)
    maxNum = max(nums)

    result = round((maxNum / minNum), 2)
    stringNumber = str(result)
    
    return stringNumber[-2:]

print(quickRound([56, 23,204, 19]))



