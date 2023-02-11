# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def insertionSortList(self, head: ListNode) -> ListNode:

    li = ListNode(0)
    temp = head

    while temp:
      prev = li
      while prev.next and prev.next.val < temp.val:
        prev = prev.next
        
      next = temp.next
      temp.next = prev.next
      prev.next = temp
      temp = next

    return li.next
