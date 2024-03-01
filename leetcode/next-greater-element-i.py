class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        mono_stack = []
        track = {}
        
        for i in range(len(nums2)):
            while mono_stack and mono_stack[-1] < nums2[i]:
                popped_item = mono_stack.pop()
                track[popped_item] = nums2[i]
            
            mono_stack.append(nums2[i])
            
        for i in range(len(nums1)):
            
            if nums1[i] in track:
                nums1[i] = track[nums1[i]]
                
            else:
                nums1[i] = -1
        
        
        return nums1
        
        
        