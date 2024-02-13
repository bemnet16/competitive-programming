# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:

        bits = []
        while head:
            bits.append(head.val)
            head = head.next
        
        answer = 0
        for i in range(len(bits)):

            decimal = ((2 ** i) * bits[-i - 1])
            answer += decimal
        
        return answer