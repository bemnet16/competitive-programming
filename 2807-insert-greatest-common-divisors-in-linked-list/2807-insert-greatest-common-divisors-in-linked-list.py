# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def findGCD(a, b):
            if b == 0:
                return a
            return findGCD(b, a % b)
        
        
        cur = head
        
        while cur.next:
            gcd = findGCD(cur.val, cur.next.val)
            new_node = ListNode(val=gcd, next=cur.next)
            cur.next = new_node
            cur = new_node.next
        
        
        return head
        