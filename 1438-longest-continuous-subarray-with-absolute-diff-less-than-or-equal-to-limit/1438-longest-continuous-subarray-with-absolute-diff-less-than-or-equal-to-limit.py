class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        _min = []
        _max = []
        freq = defaultdict(int)
        l = 0
        ans = 0

        for r, num in enumerate(nums):

            freq[num] += 1
            heappush(_min, num)
            heappush(_max, -num)
            
            while -_max[0] - _min[0] > limit:
                freq[nums[l]] -= 1
                l += 1
                
                while freq[_min[0]] == 0:
                    heappop(_min)
                    
                while freq[-_max[0]] == 0:
                    heappop(_max)
            
            ans = max(ans, r - l + 1)
        
        
        return ans
        