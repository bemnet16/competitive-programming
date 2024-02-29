class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(p) > len(s):
            return []
        
        k = len(p)
        
        p_dict = defaultdict(int)
        s_dict = defaultdict(int)
        
        # to perform comparison / check equality / of the two dicts 
        # initialize both 'p' and 's' dict with all lowercase letters with '0' value 
        for i in range(97, 123):
            char = chr(i)
            p_dict[char] = 0
            s_dict[char] = 0
            
        
        for char in p:
            p_dict[char] += 1
            
        for i in range(len(p)):
            s_dict[s[i]] += 1
        
        
        answer = []
        
        if s_dict == p_dict:
            answer.append(0)
        
        for i in range(len(s) - k):
            
            s_dict[s[i]] -= 1
            s_dict[s[i + k]] += 1
            
            if s_dict == p_dict:
                answer.append(i + 1)
        
        
        return answer
            
            
            
            
            
            
        
        
            
        