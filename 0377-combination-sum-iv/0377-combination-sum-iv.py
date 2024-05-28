class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        cache = defaultdict(int)
        
        def dp(cur):
            
            if cur == target:
                return 1
            if cur > target:
                return 0
            
            if cur in cache:
                return cache[cur]
            
            temp = 0
            for num in nums:
                cache[cur] += dp(cur + num)
            
            return cache[cur]
        
        return dp(0)