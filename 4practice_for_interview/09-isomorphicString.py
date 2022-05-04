'''Given two strings, determine if they are isomorphic. Two strings are "isomorphic" if each unique character from the first string can be replaced to match the second string, without changing the ordering of the characters.

Different characters must map to different characters, but a character can map to itself.

Input
str_1: the first string.
str_2: the second string.
Output
Whether if these two strings are isomorphic.

Examples
Example 1:
Input:

str_1 = "egg"
str_2 = "all"
Output: true

Explanation:

"e" can be replaced with "a" and "g" can be replaced with "l". Therefore, the strings are isomorphic.

Example 2:
Input:

str_1 = "wow"
str_2 = "aaa"
Output: false

'''

def solution(str1, str2):
    map1, map2 = {},{}

    # for i in range(len(str1)):
        # c1, c2 = str1[i], str2[i]
    # ether range(len()) and zip() is fine!!!! 
    if len(str1) != len(str2):
        return False
    for c1, c2 in zip(str1,str2):
        # print(c1,c2)
        if ((c1 in map1 and map1[c1] != c2) or (c2 in map2 and map2[c2] != c1)):
            return False

        map1[c1] = c2
        map2[c2] = c1
    return True

print(solution('egg','all'))#True
print(solution('woweeee','aaa'))#False
print(solution('wow','aaa'))#False
print(solution('goo','yee'))#True

