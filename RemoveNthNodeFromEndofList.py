# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        s=ListNode()
        s.next=head
        l=0
        while head:
            l+=1
            head=head.next
        l-=n
        cur=s
        for i in range(l):
            cur=cur.next
        cur.next=cur.next.next
        return s.next
