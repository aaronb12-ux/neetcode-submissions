from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        '''
        run a bfs.
            we want to store nodes as levels in the queue.

        '''
        if not root:
            return []

        ans = []
        queue = deque([root])

        while queue:

            levelLength = len(queue)
            newlevel = []

            for i in range(levelLength):

                node = queue.popleft()

                newlevel.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            ans.append(newlevel)
        
        return ans
    
            
            
                


                
        