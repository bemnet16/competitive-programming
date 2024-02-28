class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        
        pointer1 = 0
        pointer2 = 0
        
        while pointer1 < len(nums1) and pointer2 < len(nums2):
            
            if nums1[pointer1] == nums2[pointer2]:
                return nums1[pointer1]
            
            elif nums1[pointer1] < nums2[pointer2]:
                pointer1 += 1
            else:
                pointer2 += 1
        
    
        return -1
    
    
    
    
        
#         set_nums2 = set(nums2)
        
#         for num in nums1:
            
#             if num in set_nums2:
#                 return num
            
        
#         return -1
        