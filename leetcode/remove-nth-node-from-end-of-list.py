# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        
        demmy_node = ListNode()
        demmy_node.next = head
        left = demmy_node
        right = demmy_node
        
        for _ in range(n):
            right = right.next
        
        while right and right.next:
            left = left.next
            right = right.next
        
        if left.next and left.next.next:
            left.next = left.next.next
        elif not left.next.next:
            left.next = None
        
        return demmy_node.next