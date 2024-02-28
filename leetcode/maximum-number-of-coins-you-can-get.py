class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        n = len(piles)
        
        piles.sort()
        max_coins = 0
        
        for i in range(n // 3, n, 2):
            
            max_coins += piles[i]
        
        
        return max_coins
        