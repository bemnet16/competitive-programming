# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        
        current_node = head
        # Iterate through all node until it is None
        while current_node and current_node.next:
            
            next_node = current_node.next
            current_node.next = next_node.next
            next_node.next = head
            # Update the head node to the reversed node
            head = next_node
        
        return head