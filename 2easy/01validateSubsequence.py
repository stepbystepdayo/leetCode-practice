"""
Validate Subsequnce

Given two non-empty arrays of integers, write a function that determines wheather the second array as a subsequence of the first one.

A subsequence of an array is a set of numbers that aren't necessarily adacent in the array but that are in the same order as they apprear in the array. For instance, the numbers [1,3,4] from a subsequence of the array [1, 2, 3, 4], and so do the numbers [2,4]. Note that a single number in an array and the array itself are both valid subsequences of the array.

Sample input
array = [5,1,22,25,6,-1,8,10]
sequence = [1,6,-1,10]

Sample output: True

"""
# This is the solution by using while (two pointer)
def validareSubsequence(array, sequence):
    arrayIdx = 0
    seqIdx = 0
        # need to check the all of array numbers and sequence numbers
    while arrayIdx < len(array) and seqIdx < len(sequence):
        if array[arrayIdx] == sequence[seqIdx]:
            # if array's number and sequence's number are the same, move tothe next number 
            seqIdx += 1
        arrayIdx += 1
        # why we put arryIdx in outside of if condition? -> regardless of whether or not we have a match, need to check all of array
    return seqIdx == len(sequence)

# This is the solution by using for loop 
def validareSubsequenceLoop(array, sequence):
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            return True
        if sequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(sequence)
    # if seqIdx's number and len(sequence) is the same, return True


print(validareSubsequence([5,1,22,25,6,-1,8,10],[1,6,-1,10]))
print(validareSubsequenceLoop([5,1,22,25,6,-1,8,10],[1,6,-1,10]))




