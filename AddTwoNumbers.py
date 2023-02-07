# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    dums = ListNode(0)
    dum = dums
    val = 0

    while val or l1 or l2:
      if l1:
        val += l1.val
        l1 = l1.next
        
      if l2:
        val += l2.val
        l2 = l2.next
        
      dum.next = ListNode(val % 10)
      val //= 10
      dum = dum.next

    return dums.next
