class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        map_st, map_ts = defaultdict(str), defaultdict(str)
        
        for char_s, char_t in zip(s, t):
            
            if (char_s in map_st and map_st[char_s] != char_t) or (char_t in map_ts and map_ts[char_t] != char_s):
                return False
            
            map_st[char_s] = char_t
            map_ts[char_t] = char_s
        
        
        return True
            
            
        
#         charmap = defaultdict(str)
#         reserved = set()
        
#         for i in range(len(s)):
            
#             if s[i] not in charmap and t[i] not in reserved:
#                 charmap[s[i]] = t[i]
#                 reserved.add(t[i])
          
        
#         chars = []
        
#         for c in s:
#             chars.append(charmap[c])
        
#         return "".join(chars) == t