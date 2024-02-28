class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        set_nums2 = set(nums2)
        
        for num in nums1:
            
            if num in set_nums2:
                return num
            
        
        return -1
        