# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        d={}
        cur=head
        while cur:
            d[cur]=cur.val
            cur=cur.next
        for i in d:
            i.next=None
        l=sorted(d.items(), key=lambda x:x[1])
        nn=ListNode()
        cur=nn
        for n,i in l:
            cur.next=n
            cur=cur.next
        return nn.next
