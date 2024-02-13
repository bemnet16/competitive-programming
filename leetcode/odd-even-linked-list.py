# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Initialize demmy node for odd indices and even indices
        demmy_odd = ListNode()
        demmy_even = ListNode()

        # Initialize head for odd and even demmy nodes to track of the current node
        odd_head = demmy_odd
        even_head = demmy_even

        # Helper function to identify the oddness and evenness of indcies
        def isOdd(index):
            if index % 2 == 0:
                return False
            return True

        # The fist node is considers as odd
        index = 1

        while head:

            if isOdd(index):
                odd_head.next = head
                head = head.next
                odd_head = odd_head.next
                odd_head.next = None
            
            else:
                even_head.next = head
                head = head.next
                even_head = even_head.next
                even_head.next = None
            
            # increment the index
            index += 1
        
        # append even nodes to the right of odd nodes
        odd_head.next = demmy_even.next

        # return the updated head
        return demmy_odd.next

        