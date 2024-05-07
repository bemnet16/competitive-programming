# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        demmy_node = ListNode(float("inf"))
        stk = [demmy_node]
        
        cur = head
        while cur:
            
            while cur.val > stk[-1].val:
                stk.pop()
            
            stk[-1].next = cur
            stk.append(cur)
            cur = cur.next
        
        return stk[0].next
        