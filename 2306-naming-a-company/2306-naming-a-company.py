class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        
        hashSet = defaultdict(set)
        for idea in ideas:
            hashSet[idea[0]].add(idea[1:])
        
        
        ans = 0
        
        for prefix in hashSet:
            for nx_pre in hashSet:
            
                common = 0
                
                for suffix in hashSet[nx_pre]:
                    if suffix in hashSet[prefix]:
                        common += 1
                
                ans += (len(hashSet[prefix]) - common) * (len(hashSet[nx_pre]) - common)
        
        
        return ans
            