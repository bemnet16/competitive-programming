# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        d,i={},1
        cur=head
        while cur:
            d[i]=cur
            cur=cur.next
            i+=1
            
        d[k].val,d[len(d)-k+1].val=d[len(d)-k+1].val,d[k].val
        return head
