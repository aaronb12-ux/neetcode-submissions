# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        '''
                on every path we need to keep track of the greatest node.
                if the current node, is greater than this greatest node, thats a good node. then update the current node.

        '''

        self.good_nodes = 0

        def dfs(node, greatest_node):

            if not node:
                return
            
            if node.val >= greatest_node:
                self.good_nodes += 1
                greatest_node = node.val
            
            dfs(node.left, greatest_node)
            dfs(node.right, greatest_node)
        
        dfs(root, root.val)
        
        return self.good_nodes
            




        