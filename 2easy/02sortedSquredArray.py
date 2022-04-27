"""
-Srorted Aquared Array-
Write a function that takes in a non-empty array of integers that are sorted in ascending order and returns a new array of the same length with the aquares of the originl integers also sorted in ascending order.
"""



def sortedSquaredArry(array):
    # need to make 0 in array
    sortedSquares = [0 for _ in array]
    # make twopointers smallestValue is going to start 0
    smallerValueIdx = 0
    # largest value is going to start end of value 
    largerValueIdx = len(array) -1

    for index in reversed(range(len(array))):
        # print(index)
        smallValue = array[smallerValueIdx]
        largeValue = array[largerValueIdx]

        if abs(smallValue) > abs(largeValue):
            sortedSquares[index] = smallValue * smallValue
            smallerValueIdx += 1
        else:
            sortedSquares[index] = largeValue * largeValue
            largerValueIdx -= 1

    return sortedSquares

print(sortedSquaredArry([1,2,3,4,5,6,7,8,9])) #[1,4,9,25,36,49,64,81]
print(sortedSquaredArry([1,4,7,5,6,2,8,3,9]))#[1,4,9,25,36,49,64,81]