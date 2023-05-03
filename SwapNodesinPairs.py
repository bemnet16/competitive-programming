# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        temp_node=ListNode()
        temp_node.next=head
        cur=temp_node
        while cur.next and cur.next.next:
            idx_1=cur.next
            idx_2=idx_1.next
            idx_1.next=idx_2.next
            idx_2.next=idx_1
            cur.next=idx_2
            cur=idx_1
        return temp_node.next    
