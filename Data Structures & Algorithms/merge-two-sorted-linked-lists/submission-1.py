# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        prev = dummy

        curr1 = list1
        curr2 = list2

        while curr1 is not None and curr2 is not None:

            val1 = curr1.val
            val2 = curr2.val

              
            if val1 < val2:
                prev.next = curr1
                prev = prev.next
                curr1 = curr1.next
            
            elif val2 < val1:
                prev.next = curr2
                prev = prev.next
                curr2 = curr2.next

            else:
                prev.next = curr1
                curr1 = curr1.next
                prev = prev.next

                prev.next = curr2
                curr2 = curr2.next
                prev = prev.next
         
        
        if curr1 is not None:
            prev.next = curr1
        elif curr2 is not None:
            prev.next = curr2
        
        return dummy.next


                
            
        
                
                
                
                



    

            
 









        