# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cur_sum = 0
        merge_point = head
        cur = head.next
        
        while cur:
            cur_sum += cur.val
            
            if cur.val == 0:
                merge_point = merge_point.next
                merge_point.val = cur_sum
                cur_sum = 0
            
            cur = cur.next
        
        
        merge_point.next = None
        return head.next
        