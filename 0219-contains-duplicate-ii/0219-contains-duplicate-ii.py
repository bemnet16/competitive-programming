class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        freq = defaultdict(int)
        
        for i in range(min(k, len(nums))):
            if nums[i] in freq:
                return True
            freq[nums[i]] += 1
        
        for i in range(k, len(nums)):
            if freq[nums[i]] > 0:
                return True
            freq[nums[i]] += 1
            freq[nums[i - k]] -= 1
        
        return False
            