# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Initialize the 3 variables /slow, fast/ ("to check if there is a cycle") and /intersection/ ("meeting point")
        slow = head
        fast = head
        intersection = None


        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next
            
            # If slow is equal to fast they are intersecting at that point. save the node and break the loop
            if slow == fast:
                intersection = fast
                break
        
        # If there is no intersection there is no loop. /return null/
        if not intersection:
            return
        
        # tortoise /slow/, rabbit/fast/
        tortoise = head
        rabbit = intersection

        # Catch the intersection node start tortoise from these start/head/ and rabbit from the intersection node
        while tortoise != rabbit:
            tortoise = tortoise.next
            rabbit = rabbit.next
        
        # Return either tortoise or rabbit since this is the same node. / the loop start at this node/
        return tortoise
            
        