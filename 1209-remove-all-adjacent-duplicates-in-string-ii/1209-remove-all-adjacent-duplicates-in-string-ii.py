class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stk = []
        freq = defaultdict(int)
        
        for char in s:
            
            freq[char] += 1
            stk.append(char)
            
            if freq[char] >= k and len(set(stk[-k:])) == 1:
                for _ in range(k):
                    stk.pop()
                freq[char] -= k
        
        
        return "".join(stk)
                    
        