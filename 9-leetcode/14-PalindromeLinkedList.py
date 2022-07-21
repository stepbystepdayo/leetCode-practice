
'''
Given the head of a singly linked list, return true if it is a palindrome.

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false


'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        
        arr = []
        
        while head:
            arr.append(head.val)
            head = head.next
        
        s, e = 0,len(arr)-1
        
        while s <= e:
            if arr[s] != arr[e]:
                return False
            s += 1
            e -= 1
        return True