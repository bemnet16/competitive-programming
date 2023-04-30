# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        cur=head
        lg=0
        d={0:head}
        while cur.next:
            cur=cur.next
            lg+=1
            d[lg]=cur
        m_sum=0
        for i in range((lg+1)/2):
            twin=d[i].val+d[lg-i].val
            if twin>m_sum:
                m_sum=twin
        return m_sum
