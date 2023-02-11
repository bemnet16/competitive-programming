# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def nextLargerNodes(self, head: ListNode) -> List[int]:

    result = []
    li = []

    while head:
      while li and head.val > result[li[-1]]:
        index = li.pop()
        result[index] = head.val
      li.append(len(result))
      result.append(head.val)
      head = head.next

    for i in li:
      result[i] = 0

    return result
