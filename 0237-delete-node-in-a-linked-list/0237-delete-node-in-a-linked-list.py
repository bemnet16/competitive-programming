# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        
        # We need to change the value of node
        node.val = node.next.val
        
        # And then we can discard the next node from the given node
        node.next = node.next.next
        