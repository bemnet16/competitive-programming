# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        removable_nums = set(nums)
        dummy = ListNode(next = head)
        cur_node = dummy
        
        while cur_node.next:
            
            if cur_node.next.val in removable_nums:
                cur_node.next = cur_node.next.next
            else:
                cur_node = cur_node.next
        
        
        return dummy.next
        
        