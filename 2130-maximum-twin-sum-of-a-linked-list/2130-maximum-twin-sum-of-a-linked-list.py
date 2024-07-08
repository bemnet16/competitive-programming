# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        
        cur = slow.next
        slow.next = None
        slow = cur
        while slow and slow.next:
            temp = slow.next
            slow.next = temp.next
            temp.next = cur
            cur = temp
        
        ans = 0
        while cur:
            ans = max(ans, cur.val + head.val)
            cur = cur.next
            head = head.next
        
        return ans
        