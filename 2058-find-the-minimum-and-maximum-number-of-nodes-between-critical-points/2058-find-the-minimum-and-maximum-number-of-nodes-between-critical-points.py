# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        if not (head and head.next and head.next.next):
            return [-1, -1]
        
        left, mid, right = head, head.next, head.next.next
        idx = 2
        ans = [-1, -1]
        track = None
        
        while right:
            if (left.val > mid.val < right.val) or (left.val < mid.val > right.val):
                if not track:
                    track = [idx, idx]
                    ans = [float('inf'), float('-inf')]
                else:
                    ans[0] = min(ans[0], idx - track[1])
                    track[1] = idx
            
            idx += 1
            left = mid
            mid = right
            right = right.next
        
        
        if not track or ans[0] == float('inf'):
            return [-1, -1]
        
        ans[1] = track[1] - track[0]
        return ans