Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        cur = root
        count = 0
        
        while cur is not None:
            if low <= cur.val >= high:
                count += cur.val
                
                
            if low > cur.val:
                cur = cur.right
            if high < cur.val:
                cur = cur.left
        return count 
            