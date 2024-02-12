# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        
        # Store node values to check if it is plaindrome or not
        values = []
        current_node = head
        
        while current_node:
            
            values.append(current_node.val)
            current_node = current_node.next
            
            
            
        for i in range((len(values)) // 2):
            
            if values[i] != values[-i - 1]:
                return False
        
        return True