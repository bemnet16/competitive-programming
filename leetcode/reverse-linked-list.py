# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        temp = head
        while temp and temp.next:
            i = temp.next
            temp.next = i.next
            i.next = head
            head = i        
        return head