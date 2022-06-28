'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false

'''

def solution(s):
    start = 0
    end = len(s)-1

    while start < end:
        if s[start] != s[end]:
            skipS = s[start +1 : end +1]
            skipE = s[start : end]
            #neetcode kakikata
            # return(skipS == skipS[::-1] or skipE == skipE[::-1])

            # second kakikata
            # if skipS == skipS[::-1]:
            #     return True
            # if skipE == skipE[::-1]:
            #     return True
            # else:
            #     return False

            # third kakikata
            if skipS == skipS[::-1] or skipE == skipE[::-1]:
                return True
            else:
                return False
        start += 1
        end -= 1

    return True






print(solution("aba")) #true
print(solution("abca")) #true
print(solution("abc")) #False
print(solution("zbbbbbb")) #False


