'''
Validate Subsequnce

Given two non-empty arrays of integers, write a function that determines wheather the second array as a subsequence of the first one.

A subsequence of an array is a set of numbers that aren't necessarily adacent in the array but that are in the same order as they apprear in the array. For instance, the numbers [1,3,4] from a subsequence of the array [1, 2, 3, 4], and so do the numbers [2,4]. Note that a single number in an array and the array itself are both valid subsequences of the array.

Sample input
array = [5,1,22,25,6,-1,8,10]
sequence = [1,6,-1,10]

Sample output: True
'''



def isValidSubsequence(array, sequence):
    hashmap = {}
    # print(hashmap)
    # for num in array:
    #     for seqNum in sequence:
    #         if seqNum not in hashmap:
    #             hashmap[seqNum] = 0
    #         if hashmap[seqNum] == num:
    #             hashmap[seqNum] += 1
        
        




# def isValidSubsequence(array,sequence):
#     arrayNum, sequenceNum = 0,0
#     while arrayNum != len(array) and sequenceNum != len(sequence):
#         if array[arrayNum] == sequence[sequenceNum]:
#             sequenceNum += 1
#         arrayNum += 1
#     if sequenceNum >= len(sequence):
#         return True
#     return False





print(isValidSubsequence([5,1,22,25,6,-1,8,10],[1,6,-1,10]))
