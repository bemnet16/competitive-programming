class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        max_sat = 0
        ans = 0
        for cus, gru in zip(customers, grumpy):
            if gru == 0:
                ans += cus
        
        
        for i in range(minutes - 1):
            if grumpy[i] == 1:
                ans += customers[i]
        
        for i in range(minutes - 1, len(customers)):
            if grumpy[i] == 1:
                ans += customers[i]
            
            max_sat = max(max_sat, ans)
            
            if grumpy[i - minutes + 1] == 1:
                ans -= customers[i - minutes + 1]
        
        
        return max_sat
            
            