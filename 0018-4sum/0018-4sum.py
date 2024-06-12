class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        ans = set()
        
        for a in range(len(nums)):
            for b in range(a + 1, len(nums)):
                
                c = b + 1
                d = len(nums) - 1
                
                while c < d:
                    
                    sum_4 = nums[a] + nums[b] + nums[c] + nums[d]
                    
                    if sum_4 - target < 0:
                        c += 1
                    elif sum_4 - target > 0:
                        d -= 1
                    else:
                        ans.add((nums[a], nums[b], nums[c], nums[d]))
                        c += 1
                        d -= 1
        
        
        return ans
                
        
        