# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        result = []
        temp = head
        while(temp):
            result.append(temp.val)
            temp = temp.next
        return result == result[::-1]