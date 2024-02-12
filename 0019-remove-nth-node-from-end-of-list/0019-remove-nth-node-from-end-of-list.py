# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        
        # To handle if head need to be removed
        demmy_node = ListNode()
        demmy_node.next = head
        
        # Initialize the two /left, right/ poninters
        left = demmy_node
        right = demmy_node
        
        # Proceed the right pointer with the value of backward index
        for _ in range(n):
            right = right.next
        
        # Go to the end of list until there is no element next to right pointer
        while right and right.next:
            left = left.next
            right = right.next
        
        # Remove the element at index "n" from the backward 
        left.next = left.next.next
        
        return demmy_node.next