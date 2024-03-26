class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        track = defaultdict(int)
        
        for num in arr:
            
            if (k - num) % k in track:
                
                if track[(k - num) % k] == 1:
                    del track[(k - num) % k]
                else:
                    track[(k - num) % k] -= 1
            
            else:
                track[num % k] += 1
        
        
        
        return not track