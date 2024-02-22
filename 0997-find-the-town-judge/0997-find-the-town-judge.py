from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        if not trust and n == 1:
            return 1
        
        d = defaultdict(int)
        s = set()
        tot = 0
        
        for a,b in trust:
            if a not in s:
                s.add(a)
                tot += a
        
        
        exp = (n * (n + 1)) // 2
        
        if exp == tot:
            return -1
        
        judge = exp - tot
        
        d[judge] = judge
        for a,b in trust:
            if b == judge:
                d[a] = judge
            
        
        isJ = all(d[i] == judge for i in range(1, n + 1))

        if d and isJ:
            return judge
        
        return -1
        
        
            
            