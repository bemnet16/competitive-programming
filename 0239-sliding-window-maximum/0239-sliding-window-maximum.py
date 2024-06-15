class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)
        max_heap = []
        ans = []
        
        for i in range(k - 1):
            freq[nums[i]] += 1
            heappush(max_heap, -nums[i])
        
        
        for i in range(k - 1, len(nums)):
            
            freq[nums[i]] += 1
            heappush(max_heap, -nums[i])
            
            while freq[-max_heap[0]] == 0:
                heappop(max_heap)
            
            ans.append(-max_heap[0])
            freq[nums[i - k + 1]] -= 1
        
        
        return ans
        