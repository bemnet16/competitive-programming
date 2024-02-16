class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        answer = []
        
        for n in nums1:
            
            i = 0
            while i < len(nums2) and nums2[i] != n:
                i += 1
            
            while i < len(nums2) and n >= nums2[i]:
                i += 1
            
            if i == len(nums2):
                answer.append(-1)
            else:
                answer.append(nums2[i])
        
        return answer
            
                
        