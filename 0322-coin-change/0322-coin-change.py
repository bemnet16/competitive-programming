class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        lis = [float("inf")] * (amount + 1)
        lis[0] = 0
        
        
        for coin in coins:
            for i in range(coin, amount + 1):
                
                    lis[i] = min(lis[i], 1 + lis[i - coin])
        
        
        return lis[amount] if lis[amount] < float("inf") else -1