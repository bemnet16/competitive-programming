# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        cur=head
        lg=1
        while cur.next:
            lg+=1
            cur=cur.next
        lg//=2
        for i in range(lg):
            head=head.next
        return head
            
