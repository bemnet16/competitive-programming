from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        if not trust and n == 1:
            return 1
        
        d = defaultdict(int)
        
        # store numbers that we haven't seen yet
        s = set()
        
        # prefix sum /total/ 
        tot = 0
        
        for a,b in trust:
            if a not in s:
                s.add(a)
                tot += a
        
        # expected sum that contains every numbers
        exp = (n * (n + 1)) // 2
        
        # if all numbers are present there is no judge
        if exp == tot:
            return -1
        
        # judge will be the missing number 
        judge = exp - tot
        
        
        for a,b in trust:
            if b == judge:
                d[a] = judge
                
        # if judge is a number in 'n' inorder not to affect isJudge 
        d[judge] = judge
        
        # check if there is a least one number that doesn't trust judge 
        isJudge = all(d[i] == judge for i in range(1, n + 1))

        if d and isJudge:
            return judge
        
        return -1
        
        
            
            