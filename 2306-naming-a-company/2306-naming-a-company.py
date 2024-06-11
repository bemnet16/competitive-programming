class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        
        hashSet = defaultdict(set)
        for idea in ideas:
            hashSet[idea[0]].add(idea[1:])
        
        
        ans = 0
        
        for char1 in hashSet:
            for char2 in hashSet:
                
                if char1 == char2:
                    continue
            
                common = 0
                
                for suffix in hashSet[char2]:
                    if suffix in hashSet[char1]:
                        common += 1
                
                ans += (len(hashSet[char1]) - common) * (len(hashSet[char2]) - common)
        
        
        return ans
            