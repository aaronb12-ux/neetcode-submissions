from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        #do a level order traversal. and return the very right (last) nodes in the list of levels
        if not root:
            return []

        levels = []
        queue = deque([root])
        ans = []

        while queue:

            level_len = len(queue)
            new_level = []

            for i in range(level_len):


                node = queue.popleft()

                if i == level_len - 1:
                    ans.append(node.val)

                new_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            levels.append(new_level)

        
        return ans
        
        


        