# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        
        list2start = list2
        list2end = list2
        
        while list2end and list2end.next:
            list2end = list2end.next
        
        
        a_th_node = list1

        i = 1
        while i < a:
            a_th_node = a_th_node.next
            i += 1
        
        b_th_node = a_th_node
        
        while i <= b:
            b_th_node = b_th_node.next
            i += 1
        
        
        a_th_node.next = list2start
        list2end.next = b_th_node.next
        
        
        return list1