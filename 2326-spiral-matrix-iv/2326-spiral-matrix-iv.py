# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:

        # Initialize m x n matrix filled with '-1'
        matrix = [[-1 for _ in range(n)] for _ in range(m)]

        # index values for the 4 directions
        top = 0             # top forward row
        right = n - 1       # right downward column
        bottom = m - 1      # bottom backward row
        left = 0            # left upward column

        while head:

            for i in range(left, (right + 1)):
                if head:
                    matrix[top][i] = head.val
                    head = head.next
                else:
                    break
            
            for j in range((top + 1), bottom):
                if head:
                    matrix[j][right] = head.val
                    head = head.next
                else:
                    break
            
            for k in range(right, (left - 1), -1):
                if head:
                    matrix[bottom][k] = head.val
                    head = head.next
                else:
                    break
            
            for l in range((bottom - 1), top, -1):
                if head:
                    matrix[l][left] = head.val
                    head = head.next
                else:
                    break
            
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        
        return matrix


        
