# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if k==1: return head
        cur=head
        lg=1
        d={1:head}
        while cur.next:
            cur=cur.next
            lg+=1
            d[lg]=cur
            
        lg//=k
        temp=d[lg*k].next
        for i in range(lg*k):
            d[i+1].next=None
            
        nn=ListNode()
        cur=nn
        for i in range(lg):
            for j in range(k,0,-1):
                cur.next=d[j+(k*i)]
                cur=cur.next
        cur.next=temp
        return nn.next