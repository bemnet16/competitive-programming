class Node:
    def __init__(self,val=0):
        self.next = None
        self.val = val

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        # hold negative and positive integers separatly
        negative_node = Node()
        positive_node = Node()
        
        p_head = positive_node
        n_head = negative_node
        
        
        for num in nums:
            
            new_node = Node(num)
            
            if num > 0:
                p_head.next = new_node
                p_head = p_head.next
            else:
                n_head.next = new_node
                n_head = n_head.next
                
        
        positive_node = positive_node.next
        negative_node = negative_node.next
        
        for i in range(len(nums)):
            
            # strart from positive integers for even indexed points 
            if i % 2 == 0:
                nums[i] = positive_node.val
                positive_node = positive_node.next
            else:
                nums[i] = negative_node.val
                negative_node = negative_node.next
        
        return nums
                
        
        
        
        