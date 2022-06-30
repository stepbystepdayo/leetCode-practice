'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''


def solution(strs):
    result = ""

    for i in range(len(strs[0])):
        for word in strs:
            # if strs[0]'s index is the same len(word) or first word and word's chars are not eaqul Return result. 
            if i == len(word) or strs[0][i] != word[i]:
                return result
            
        result += strs[0][i]
    return result





print(solution(["flower","flow","flight"])) # fl
print(solution(["dog","racecar","car"])) # ""
print(solution(["kai","kao","karintou"])) # ka