'''Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

example:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 

'''

def solution(chars):
    # need to make hashmap for counting how many chras are there.
    hashmap = {}
    for char in chars:
        # print(pattern)
        if char not in hashmap:
            hashmap[char] = 0
        if char in hashmap:
            hashmap[char] += 1
    print(hashmap)
    for value in set(hashmap.values()):
        print(value)


    # start = 0
    # end = len(patterns)-1
    # hashmap = {}

    # print(start, end)
    # while start < end:
    #     if patterns[start] == patterns[end]:
            


    

        



            

        
        

        



print(solution("ababab"))# True
print(solution("aba"))# False
print(solution("abcabcabcabc"))# True