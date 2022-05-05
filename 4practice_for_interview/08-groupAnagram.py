
'''Given a list of strings, return a list of string lists that groups all anagrams together. Two strings are anagrams if rearranging one string results in another. For the purpose of this question, a string is an anagram of itself.

Each group of anagrams should be in alphabetical order. The output should be in alphabetical order by the first elements of each group of anagrams.

Input
strs: a list of strings.
Output
A list of string lists representing the grouped anagrams.

Examples
Example 1:
Input:


Output: [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
'''

import string


strs = ["eat" ,"tea", "tan", "ate", "nat", "bat"]

def solution(chars):
    hash = {}
    for word in chars:
        d = dict.fromkeys(string.ascii_lowercase, 0)
        for letter in word:
            d[letter] += 1
        frozen = tuple(d.items())

        if frozen not in hash:
            hash[frozen] = []

        hash[frozen].append(word)
    return hash.values()


print(solution(strs))