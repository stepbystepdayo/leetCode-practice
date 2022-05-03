'''For this question we ask you to determine whether or not a string has valid parentheses. A string has valid parentheses if each bracket is closed and opened in the same order and has the same type. Parentheses has 3 types (), {} and []

Input
s: String containing the parentheses
Output
Whether or not the string is valid

Examples
Example 1:
Input:

s = ()
Output: true

Explanation:

This is a valid parentheses sequence.

Example 2:
Input:

s = (}
Output: false

'''

def solution(parentheses):
    # make the stack to store the parentheses 
    stack = []
    # make the defalut to what kinf of parentathese are there in hashmap the, we can check these.
    # also, we need to check the close parentathese like these (,{,[. because if we found ),},] first thats mean these can not find (,{,[.
    closeToOpen = {')':'(','}':'{',']':'['}

    for pare in parentheses:
        if pare in closeToOpen:
            if stack and stack[-1] == closeToOpen[pare]:
                stack.pop()
            else:
                return False
        else:
            stack.append(pare)
    return True if not stack else False
    




print(solution('()')) #True
print(solution('()[]{')) #False
print(solution('[]'))# True