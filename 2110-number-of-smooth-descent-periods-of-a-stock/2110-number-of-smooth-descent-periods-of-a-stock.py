class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        
        count = defaultdict(int)
        count[len(prices) - 1] = 1
        ans = 1
        
        for i in range(len(prices) - 2, -1, -1):
            count[i] = 1
            if prices[i] == prices[i + 1] + 1:
                count[i] += count[i + 1]
            
            ans += count[i]
        
        
        return ans
            
        