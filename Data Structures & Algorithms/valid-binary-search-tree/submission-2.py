# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        '''
            traverse the entire tree
            if the node.left.val of the current node is greater, return False for that left subtree. vice verse for the right. we do this for all subtrees and return left and right to verify both l and r subtrees are vali
        '''

        def in_order(node, nodes):

            #do an in-order traversal of the tree and see if it is sorted

            if not node:
                return
            
            in_order(node.left, nodes)

            nodes.append(node.val)

            in_order(node.right, nodes)

            return nodes


        nodes = in_order(root, [])

        
        for i in range(0, len(nodes) - 1): 

            if nodes[i] >= nodes[i + 1]:
                return False
        
        return True
        

            

            
            
                    
            
            
            



        