# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        '''
                using the set approach

                add a node to a set. if we come across that node again then we have a cylce. this works but its O(m) space


        '''

        visited = set()

        curr = head

        while curr is not None:

            if curr.val in visited and curr.next is not None:
                return True
            else:
                visited.add(curr.val)
                curr = curr.next
        
        return False



        