class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        hashSet = {}
        
        for cA, cB in paths:
            hashSet[cA] = cB
        
        cur = paths[0][0]

        while cur in hashSet:
            cur = hashSet[cur]
        
        return cur
        