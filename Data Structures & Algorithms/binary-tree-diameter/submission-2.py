# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        #at each node in the tree, run a dfs to find the left and right subtree, and add then, if that is greater than the curr diameter, the update it

        self.diameter = 0

        def dfs(node):

            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            currDiam = left + right

            self.diameter = max(currDiam, self.diameter)

            return max(left, right) + 1

        dfs(root)

        return self.diameter

        
        




        