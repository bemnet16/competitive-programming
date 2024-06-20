class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        worker.sort()
        min_heap = []
        
        for dif, pro in zip(difficulty, profit):
            heappush(min_heap, (dif, pro))
            
        
        ans = 0
        max_profit = 0
        for ability in worker:
            
            while min_heap and min_heap[0][0] <= ability:
                max_profit = max(max_profit, heappop(min_heap)[1])
            
            ans += max_profit
        
        return ans
            