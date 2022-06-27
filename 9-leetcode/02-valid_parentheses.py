'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

'''

def solution(s):
    parens = {")":"(","]":"[","}":"{"}
    stack = []

    for p in s:
        if p in parens:
            if stack and stack[-1] == parens[p]:
                stack.pop()
            else:
                return False
        else:
            stack.append(p)
    return True if not stack else False


    




print(solution("()"))
print(solution("()[]{}"))
print(solution("(]"))
print(solution("]"))
