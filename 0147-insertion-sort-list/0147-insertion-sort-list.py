# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # length of the linked list
        n = 0
        count_head = head

        # count the length
        while count_head:
            n += 1
            count_head = count_head.next

        # Initialize a demmy linkedlist with the value less than the edge case
        demmy_node = ListNode(-5001)
        demmy_node.next = head

        # Iterate until all values are sorted / no changes encounter /
        for i in range(n - 1):
            
            # entry point for the element whose value is less than the current value
            head_reference = demmy_node

            # always start from the head - /the original linkedlist / 
            current_node = demmy_node.next

            # The last "i" elements are already sorted /no need to iterate over them/
            for j in range(n - i - 1):

                next_node = current_node.next
                if current_node.val > next_node.val:
                    current_node.next = next_node.next
                    next_node.next = current_node
                    head_reference.next = next_node
                    head_reference = head_reference.next

                # move one element up for both head ref. and current node since the two elements are sorted
                else:
                    current_node = next_node
                    head_reference = head_reference.next
            
        # return the sorted linkedlist head
        return demmy_node.next


        