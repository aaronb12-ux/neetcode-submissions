# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        '''
            run a dfs, and for each node, check the two heights. if the abs values of the differene of the two heights is 1 or less, return true, else false
        '''
        self.values = []

        if not root:
            return True

        def dfs(node):

            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            

            if abs(left - right) <= 1:

                self.values.append(True)
            
            else:
                self.values.append(False)
            
            return max(left, right) + 1

    
        dfs(root)

        for v in self.values:
            if v == False:
                return False
        
        return True




        