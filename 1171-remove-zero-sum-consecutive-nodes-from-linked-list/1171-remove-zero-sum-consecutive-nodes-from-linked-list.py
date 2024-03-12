# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        demmy = ListNode()
        demmy.next = head
        
        
        start = demmy
        
        
        while start:
            end = start.next
            prefix_sum = 0
            
            while end:
                prefix_sum += end.val
            
                if prefix_sum == 0:
                    start.next = end.next
                end = end.next
            
            start = start.next
        
        
        return demmy.next
        
                
            
        
        
        