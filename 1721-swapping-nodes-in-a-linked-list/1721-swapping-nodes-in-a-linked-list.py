# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(next=head)
        left = dummy
        right = dummy
        
        for _ in range(k):
            right = right.next
            
        first_k = right
        
        while right:
            left = left.next
            right = right.next
        
        first_k.val, left.val = left.val, first_k.val
        
        return head
        
        
        