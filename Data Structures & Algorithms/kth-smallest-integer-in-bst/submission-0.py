# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        '''
            do an in order traversal and put elements in an array. Then
            return the kyth value in that
        '''

        def inOrder(node, nodes):

            if not node:
                return
            
            inOrder(node.left, nodes)

            nodes.append(node.val)

            inOrder(node.right, nodes)

            return nodes
        
        nodes = inOrder(root, [])

        return nodes[k - 1]

        