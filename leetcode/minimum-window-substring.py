class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""
        
        left_idx = 0
        right_idx = len(s) + 1
        left = 0
        min_len = float("inf")
        
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        
        
        for i in range(65, 91):
            
            char = chr(i)
            s_dict[char] = 0
            t_dict[char] = 0
        
        
        for i in range(len(t)):
            
            s_dict[s[i]] += 1
            t_dict[t[i]] += 1
        
        
        if s_dict == t_dict:
            return s[:len(t)]
            
            
        
        def isSubString():
            
            for k in t_dict:
                if s_dict[k] < t_dict[k]:
                    return False
            
            return True
            
        
        
        for i in range(len(t), len(s)):
            
            s_dict[s[i]] += 1
            
            while isSubString():
                if i - left_idx + 1 < min_len:
                    right_idx = i
                    left = left_idx
                    min_len = i - left_idx + 1
                    
                s_dict[s[left_idx]] -= 1
                left_idx += 1
        
        
        return s[left:right_idx + 1] if min_len <= len(s) else ""
                
                
            
            
            
                
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        
        
        
        