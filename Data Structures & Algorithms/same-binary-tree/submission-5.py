# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        self.pTree = []
        self.qTree = []

        def preOrder(node, tree):

            if not node:
                if tree == "p":
                    self.pTree.append("null")
                if tree == "q":
                    self.qTree.append("null")
                return

            if tree == "p":
                self.pTree.append(node.val)
            if tree == "q":
                self.qTree.append(node.val)
                
            preOrder(node.left, tree)
    
            preOrder(node.right, tree)
        
        preOrder(p, "p")
        preOrder(q, "q")

        return self.pTree == self.qTree