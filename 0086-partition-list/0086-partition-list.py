# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        # Initialalize demmy node for the values less than/before/ and greater/after/ than "X"
        demmy_before = ListNode()
        demmy_after = ListNode()

        # Initialze the head of the two demmy nodes
        head_before = demmy_before
        head_after = demmy_after

        while head:
            
            if head.val < x:
                head_before.next = head
                head = head.next
                head_before = head_before.next
                head_before.next = None
            
            else:
                head_after.next = head
                head = head.next
                head_after = head_after.next
                head_after.next = None
            
        # append the nodes that are greater than or equal to "x" to the nodes less than "x"
        head_before.next = demmy_after.next

        # return the partitioned nodes head
        return demmy_before.next 

        