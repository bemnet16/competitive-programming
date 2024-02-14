class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        dict1 = {}
        dict2 = {}
        
        set2 = set(nums2)
        
        for num in nums1:
            dict1[num] = dict1.get(num, 0) + 1
        
        for num in nums2:
            dict2[num] = dict2.get(num, 0) + 1
        
        answer = []
        
        for num in set2:
            if num in dict1:
                times = min(dict1[num], dict2[num])
                for i in range(times):
                    answer.append(num)
        
        return answer
        