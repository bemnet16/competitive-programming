# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return
        
        length = 0
        cur = head
        last = None
        while cur:
            length += 1
            last = cur
            cur = cur.next
        
        k %= length
        cur = head
        i = 1
        
        
        while i < (length - k):
            i += 1
            cur = cur.next
        
        last.next = head
        head = cur.next
        cur.next = None
        
        return head