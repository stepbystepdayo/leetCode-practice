'''Write a function that takes in a non-empty array of integrs that are sorted in ascending order and returns a new array of the same length with the squares of the original integers also sorted in ascending order'''


# this is the brute force answer
# def solution(array):
#     output =[]
#     for num in array: # O(n) time complexity
#         output.append(num**2)
#     return sorted(output) # O(n)log(n) => fastest sorting algorithm

# without using sorting function




def solution(array):
    # we need to set up the empty array has numbers of spaces in array
    output = [0] * len(array)
    # make 2 pointers 
    start, end = 0,len(array)-1
    outputPointer = len(array)-1

    while start < end:
        # startSquared,endSquared = start**2, end**2
        # print(startSquared,endSquared)
        if array[start] < array[end]:
            output[outputPointer] = array[end]**2
            outputPointer -= 1
            end -= 1
        if array[start] > array[end]:
            output[outputPointer] = array[start]**2
            outputPointer -= 1
            start += 1
        
    print(output)
    # return output
        





print(solution([1,2,3,5,6,8,9]))
print(solution([5,7,10,20,30,40]))
print(solution([3,1,2,5]))