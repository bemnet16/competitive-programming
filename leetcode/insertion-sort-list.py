# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Initialize a demmy linkedlist with the value less than the edge case
        demmy_node = ListNode(-5001)
        demmy_node.next = head

        # Assigne a flag for the break point of the loop
        hasChange = True

        # Iterate until all values are sorted / no changes encounter /
        while hasChange:
            
            # entry point for the element whose value is less than the current value
            head_reference = demmy_node

            # always start from the head - /the original linkedlist / 
            current_node = demmy_node.next

            # always assume as it is sorted
            hasChange = False

            while current_node and current_node.next:

                next_node = current_node.next
                if current_node.val > next_node.val:
                    current_node.next = next_node.next
                    next_node.next = current_node
                    head_reference.next = next_node
                    head_reference = head_reference.next

                    hasChange = True
                
                # move one element up for both head ref. and current node since the two elements are sorted
                else:
                    current_node = next_node
                    head_reference = head_reference.next
            
        # return the sorted linkedlist head
        return demmy_node.next


        