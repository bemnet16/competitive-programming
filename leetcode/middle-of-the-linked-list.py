# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        
        # Assigne two pointer one moves two ahead each time the other only one
        slow_pointer = head
        fast_pointer = head
        
        while fast_pointer and fast_pointer.next:
            
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        
        return slow_pointer