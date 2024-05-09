class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        
        half = total_sum // 2
        pos = {0}
        
        for i in range(len(nums) - 1, -1, -1):
            
            for p in pos.copy():
                if p + nums[i] == half:
                    return True
                
                if p + nums[i] not in pos:
                    pos.add(p + nums[i])
        
        
        return False
            
            
            
        
        
        
        
#         total_sum = sum(nums)
#         if total_sum % 2 != 0:
#             return False
        
#         cache = [False] * len(nums)
#         half = total_sum // 2
        
        
#         def dp(cur, i):
            
#             if i >= len(nums) or cache[i]:
#                 return
            
#             if cur == half:
#                 return True
            
#             if cur > half:
#                 return
            
#             for j in range(i, len(nums)):
#                 dp(cur + nums[j], j + 1)
            
#             cache[i] = True
        
        
#         for i in range(len(nums)):
#             if dp(nums[i], i + 1):
#                 return True
        
#         return False