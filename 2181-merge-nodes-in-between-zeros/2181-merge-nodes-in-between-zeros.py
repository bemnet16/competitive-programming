# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        merged = ListNode()
        merged_head = merged
        cur_sum = 0
        cur = head.next
        
        while cur:
            cur_sum += cur.val
            
            if cur.val == 0:
                merged_head.next = ListNode(cur_sum)
                merged_head = merged_head.next
                cur_sum = 0
            
            cur = cur.next
        
        
        return merged.next
        