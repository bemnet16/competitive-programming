class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        ans = set()
        
        
        def twoSum(cur, i, j, t):
            while i < j:
                if nums[i] + nums[j] + t < 0:
                    i += 1
                elif nums[i] + nums[j] + t > 0:
                    j -= 1
                else:
                    cur.append(nums[i])
                    cur.append(nums[j])
                    ans.add(tuple(sorted(cur)))
                    cur.pop()
                    cur.pop()
                    i += 1
                    j -= 1
                
        
        def kSum(cur, k, idx, t):
            
            if k == 2:
                twoSum(cur, idx, len(nums) - 1, t)
                return
            
            for i in range(idx, len(nums)):
                cur.append(nums[i])
                kSum(cur, k - 1, i + 1, t + nums[i])
                cur.pop()
                
        
        kSum([], 4, 0, -target)
        return ans