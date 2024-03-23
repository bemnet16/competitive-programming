# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        if not head.next: return head
        d,lg={},0
        cur=head
        while cur.next:
            cur=cur.next
            lg+=1
            d[lg]=cur
        for i in d:
            d[i].next=None
        if lg%2==1:
            head.next=d[lg]
            cur=head.next
            lg-=1
            for i in range(lg//2):
                cur.next=d[i+1]
                cur=cur.next
                cur.next=d[lg-i]
                cur=cur.next
        else:
            cur=head
            for i in range(lg//2):
                cur.next=d[lg-i]
                cur=cur.next
                cur.next=d[i+1]
                cur=cur.next
        return head