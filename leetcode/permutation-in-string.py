class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l1 = len(s1)
        l2 = len(s2)
        
        if l1 > l2:
            return False
        
        s1_dict = defaultdict(int)
        s2_dict = defaultdict(int)
        
        for i in range(97, 123):
            
            char = chr(i)
            s1_dict[char] = 0
            s2_dict[char] = 0
            
        
        for s in s1:
            s1_dict[s] += 1
        
        
        for i in range(l1):
            s2_dict[s2[i]] += 1
        
        
        if s1_dict == s2_dict:
            return True
        
        for i in range(l1, l2):
            
            s2_dict[s2[i - l1]] -= 1
            s2_dict[s2[i]] += 1
            
            if s1_dict == s2_dict:
                return True
        
        return False
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        