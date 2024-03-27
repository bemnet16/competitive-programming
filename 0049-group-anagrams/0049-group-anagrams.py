class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list)
        
        for s in strs:
            
            charcount = defaultdict(int)
            
            for char in s:
                charcount[char] += 1
            
            
            charcount = tuple(sorted(charcount.items(), key=lambda x:x[0]))
            anagrams[charcount].append(s)
        
        
        return anagrams.values()
        
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    