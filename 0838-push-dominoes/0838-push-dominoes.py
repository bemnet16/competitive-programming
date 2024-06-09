class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        ans = list(dominoes)
        cur = 'R'
        count = 0
        
        for i in range(len(dominoes) - 1, -1, -1):
            
            d = dominoes[i]
            
            if d == '.':
                count += 1
                if cur == 'L':
                    ans[i] = 'L'
            
            elif d == 'R':
                if cur == 'R':
                    for j in range(i, i + count + 1):
                        ans[j] = 'R'
                
                elif cur == 'L':
                    for j in range(i, i + (count // 2) + 1):
                        ans[j] = 'R'
                    if count % 2:
                        ans[i + (count // 2) + 1] = '.'
                
                cur = 'R'
                count = 0
            
            
            elif d == 'L':
                cur = 'L'
                count = 0
        
        
        return "".join(ans)
            
        