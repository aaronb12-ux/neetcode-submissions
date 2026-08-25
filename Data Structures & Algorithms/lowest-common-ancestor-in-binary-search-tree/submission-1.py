# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        '''
        we have a BST
        for a node, all nodes to the right are greater and all nodes left are lower


        '''

        self.pPath = []
        self.qPath = []


        def dfsP(node):
            
            if not node:
                return
            
            self.pPath.append(node)
        
            if node.val == p.val:
                return 
            
            if p.val < node.val:

                dfsP(node.left)
    
            else:
                dfsP(node.right)
        
        def dfsQ(node):

            if not node:
                return
            
            self.qPath.append(node)
     
            if node.val == q.val:
                return
            
            if q.val < node.val:

                dfsQ(node.left)
            
            else:
                dfsQ(node.right)
        
        dfsP(root)
        dfsQ(root)

        deepest = None

        for i in range(min(len(self.pPath), len(self.qPath))):

            if self.pPath[i].val == self.qPath[i].val:
                deepest = self.pPath[i]
        
        return deepest

            

        
             
            
        '''
        [5, 3] -> return the lowest that exists in both
        [5, 8]


        [5, 3, 4] -> return the lowest -> 3
        [5, 3]
        '''


            
            
            
        