class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        freq_track = defaultdict(int)
        max_freq = 0
        total_freq = 0
        
        for num in nums:
            
            freq_track[num] += 1
            
            if freq_track[num] > max_freq:
                max_freq = freq_track[num]

                
        for key, val in freq_track.items():
            
            total_freq += (val if val == max_freq else 0)
        
        
        
        return total_freq
        