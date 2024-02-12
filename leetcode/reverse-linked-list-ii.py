# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        # create a demmy node as a padding for the ease of use
        demmy_node = ListNode()
        demmy_node.next = head

        # Initialize the head reference from which reverse start. and current node to hold current node
        head_reference = None
        current_node = demmy_node

        # Pin point the start point to reverse the linked list
        for _ in range(left):
            head_reference = current_node
            current_node = current_node.next
        

        # Reverse the sub - LinkedList from left to right
        for _ in range(right - left):
            next_node = current_node.next
            current_node.next = next_node.next
            next_node.next = head_reference.next
            head_reference.next = next_node
        
        # Return the modified head of the linked list
        return demmy_node.next
            



    