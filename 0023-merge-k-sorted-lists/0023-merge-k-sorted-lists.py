# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        
        mergedList = []
        
        for lis in lists:
            
            head = lis
            while head:
                heappush(mergedList, head.val)
                head = head.next
                
                
                
        
        demmyNode = ListNode()
        head = demmyNode
        
        
        while mergedList:
            
            head.next = ListNode(heappop(mergedList))
            head = head.next
        
        
        return demmyNode.next
        