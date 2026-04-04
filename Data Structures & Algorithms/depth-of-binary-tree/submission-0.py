# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root,curr):
            if(root is None):
                return 0
            
            left=dfs(root.left,curr)
            right=dfs(root.right,curr)
            curr=max(left,right)+1
            return curr
        return dfs(root,0)