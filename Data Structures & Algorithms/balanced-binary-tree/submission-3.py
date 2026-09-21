# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        '''
            use a dfs to find the heights of each subtree. then make sure the difference is less than or equal to 1
        '''
        balanced = [True]


        def height(root):

            if not root:
                return 0
            
            left_height = height(root.left)
            right_height = height(root.right)

            if abs(left_height - right_height) > 1:
                balanced[0] = False
                return 0
            
            return 1 + max(left_height, right_height)


        height(root)

        return balanced[0]
            



            

        