'''
You are given a string s. Consider the following algorithm applied to this string:

Take all the prefixes of the string, and choose the longest palindrome between them.
If this chosen prefix contains at least two characters, cut this prefix from s and go back to the first step with the updated string. Otherwise, end the algorithm with the current string s as a result.
Your task is to implement the above algorithm and return its result when applied to string s.

Note: you can click on the prefixes and palindrome words to see the definition of the terms if you're not familiar with them.

Example

For s = "aaacodedoc", the output should be solution(s) = "".

The initial string s = "aaacodedoc" contains only three prefixes which are also palindromes - "a", "aa", "aaa". The longest one between them is "aaa", so we cut if from s.
Now we have string "codedoc". It contains two prefixes which are also palindromes - "c" and "codedoc". The longest one between them is "codedoc", so we cut if from the current string and obtain the empty string.
Finally the algorithm ends on the empty string, so the answer is "".
For s = "codesignal", the output should be solution(s) = "codesignal".
The initial string s = "codesignal" contains the only prefix, which is also palindrome - "c". This prefix is the longest, but doesn't contain two characters, so the algorithm ends with string "codesignal" as a result.

For s = "", the output should be solution(s) = "".

'''
def solution(s):
    slow = 0
    fast = 1
    while slow < len(s):
        if s[slow] == s[fast]:
            fast += 1
        if s[slow] != s[fast]:
            deleted = s.replace(s[slow],s[slow])
            print(deleted)
            slow = fast
            fast = len(deleted) -1
            print(s[slow],s[fast])
            if slow == fast:
                slow += 1
                fast -= 1
                print(deleted)
            else:
                return ""


print(solution("aaacodedoc")) # ""
print(solution("abbab")) #b
print(solution("aaabba")) # "a"
print(solution("abbaabbaabba")) # ""

'''
def solution(s):
    slow = 0
    fast = 1
    while slow < len(s):
        if s[slow] == s[fast]:
            fast += 1
        if s[slow] != s[fast]:
            deleted = s.replace(s[slow],s[slow])
            print(deleted)
            slow = fast
            fast = len(deleted) -1
            print(s[slow],s[fast])
            if slow == fast:
                slow += 1
                fast -= 1
                print(deleted)
            else:
                return ""
                



print(s: "aaacodedoc") #""
s: "codesignal" #"codesignal"
s: "" #""
s: "abbab" # b
s: "aaabba" # "a"
s:"abbaabbaabba" #""


'''
