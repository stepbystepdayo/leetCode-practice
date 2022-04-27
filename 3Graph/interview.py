# Find all the pairs of two integers in an unsorted array that sum up to a given S. For example, if the array is [3, 5, 2, -4, 8, 11] and the sum is 7, your program should return [[11, -4], [2, 5]] because 11 + -4 = 7 and 2 + 5 = 7


def solution(array,target):
    # need to make 2 pointers
    # start = 
    # end = array[-1]
    hash = {}
    returnArray = []
    
    for num in array:
        comp = target - num
        # print(comp, target, num)
        if comp in hash:
            # return hash
            
            returnArray.append([comp, num])
            
        else:
            hash[num] = comp
            # print(hash)

    return returnArray

        # if number 5 in hash map, comp is going to be 2 so we need to find 2.

        
        




print(solution([3, 5, 2, -4, 8, 11], 7))