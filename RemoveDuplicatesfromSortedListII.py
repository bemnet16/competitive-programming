# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        nn = ListNode()
        nn.next = head
        cur = nn.next
        temp = nn
        is_duplicate = False
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next=cur.next.next
                is_duplicate = True
            else:
                cur=cur.next
                if is_duplicate:
                    temp.next = cur
                    is_duplicate = False
                else:
                    temp=temp.next
        if is_duplicate:
            temp.next = None
        return nn.next
