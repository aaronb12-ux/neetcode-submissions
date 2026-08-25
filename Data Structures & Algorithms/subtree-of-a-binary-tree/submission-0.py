# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        '''
            do a pre-order traversal of both trees to get them in order. See if subroot exist in the root
        '''
        

        def preOrder(node, order):

            if not node:
                order.append(None)
                return
            
            order.append(node.val)

            preOrder(node.left, order)
            preOrder(node.right, order)

            return order
        

        rootOrder = preOrder(root, [])
        subRootOrder = preOrder(subRoot, [])


        print("Root", rootOrder)
        print("SubRoot", subRootOrder)


        def isSubArr(rootOrder, subRootOrder): #return whether subRootOrder exists in rootOrder

            root = ",".join(map(str, rootOrder))
            subRoot = ",".join(map(str, subRootOrder))

            return subRoot in root
        
        return isSubArr(rootOrder, subRootOrder)

        
        
            