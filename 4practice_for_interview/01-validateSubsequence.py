'''
Validate Subsequnce

Given two non-empty arrays of integers, write a function that determines wheather the second array as a subsequence of the first one.

A subsequence of an array is a set of numbers that aren't necessarily adacent in the array but that are in the same order as they apprear in the array. For instance, the numbers [1,3,4] from a subsequence of the array [1, 2, 3, 4], and so do the numbers [2,4]. Note that a single number in an array and the array itself are both valid subsequences of the array.

Sample input
array = [5,1,22,25,6,-1,8,10]
sequence = [1,6,-1,10]

Sample output: True


Kai/sayo notes:

so the array is not empty! good, we dont have to check for this. if we do check, we can just see if len(array) and len(sequence is not == 0)
'''

# i will make a HELPER function, because IT HELPS ME to CHECK if they arrays are (hontoni) not empty.
# for refactoring, we should try to use *args and learn how to LOOP OVER args and check each one!!!!
# def arraysNotEmpty(array1, array2):
#     # array1.length
#     if len(array1) == 0 or len(array2) == 0 or isinstance(array1, list) == False or isinstance(array2, list) == False:
#         return False
#     else:
#         return True

# def isValidSubsequenceElite(array,subsequence):
    # first, CHECK if arrays are actually NOT EMPTY!!!

#     isEmpty = arraysNotEmpty(array, subsequence)

#     if isEmpty == False:
#         return False, "THE INPUT ARRAYS ARE EMPTY! PLEASE FIX!"

    








def isValidSubsequenceElite(array, subsequence):
    # need to make pointer
    arrayPointer, subPointer = 0,0

    while arrayPointer < len(array) and subPointer < len(subsequence):
        if array[arrayPointer] == subsequence[subPointer]:
            subPointer += 1
            arrayPointer += 1
        else:
            arrayPointer += 1
    print(arrayPointer,subPointer)

    if subPointer == len(subsequence):
        return True
    return False


print(isValidSubsequenceElite([1,2,3,4,5,6],[2,3,4]))







        




# def isValidSubsequence(array,sequence):
#     arrayNum, sequenceNum = 0,0
#     while arrayNum != len(array) and sequenceNum != len(sequence):
#         if array[arrayNum] == sequence[sequenceNum]:
#             sequenceNum += 1
#         arrayNum += 1
#     if sequenceNum >= len(sequence):
#         return True
#     return False





print(isValidSubsequenceElite([5,1,22,25,6,-1,8,10,8, 10],[1,6,-1,10, 10]))
# print(isValidSubsequenceElite([0], []))
# print(isValidSubsequenceElite([], [0]))
# print(isValidSubsequenceElite([],[]))
# print(isValidSubsequenceElite("hi", "im kai and im handsome"))