# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Start with a demmy node to append sorted list
        demmy_node = ListNode()
        
        # Initialize the head of those three linked lists
        demmy_head = demmy_node
        head_1 = list1
        head_2 = list2
        
        # Iterete until we get none for either of the linked list
        while head_1 and head_2:
            
            # Find the minimum value and append the node to the demmy node
            if head_1.val <= head_2.val:
                demmy_head.next = head_1
                head_1 = head_1.next
            else:
                demmy_head.next = head_2
                head_2 = head_2.next
            
            # Update the demmy head to the appended node
            demmy_head = demmy_head.next
        
        # Check if there is a remaining nodes from those two linked lists
        if head_1:
            demmy_head.next = head_1
        else:
            demmy_head.next = head_2
        
        
        return demmy_node.next
        
        