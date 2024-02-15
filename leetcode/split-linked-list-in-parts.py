# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        # count the length of the linkedlist /"n"/
        n = 0
        current_node = head

        while current_node:
            n += 1
            current_node = current_node.next
        
        quotient = n // k  ## Every list should have a length of /quotient/ elements
        reminder = n % k   ## The first /reminder/ lists have an extra 1 elements
        current_node = head
        answer = []   ## Store the answer or the first node of each lists

        # There are k lists we need to append to the /answer/
        for _ in range(k):

            # add extra '1' elements for the first /reminder/ lists
            extra = 0
            if reminder > 0:
                extra = 1
                reminder -= 1
            
            # initialilze and assume the edge case
            temp_node = None
            for i in range(quotient + extra):
                
                temp_node = current_node
                current_node = current_node.next

                # append the first node to the /answer/
                if i == 0:
                    answer.append(temp_node)

            # remove the nodes comes from the last node of each list else append None if no node
            if temp_node:
                temp_node.next = None
            else:
                answer.append(None)

        
        return answer

        