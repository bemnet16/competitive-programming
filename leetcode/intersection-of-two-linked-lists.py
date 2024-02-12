# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        
        # Save all val - Node value of linkedListA
        track_list_1 = set()
        
        while headA:
            track_list_1.add(headA)
            headA = headA.next
        
        while headB:
            if headB in track_list_1:
                return headB
            headB = headB.next
        
        return
            
        