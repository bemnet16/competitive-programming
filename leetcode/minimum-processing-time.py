class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        
        processorTime.sort(reverse = True)
        tasks.sort()
        
        min_time = float("-inf")
        
        for i in range(len(processorTime)):
            for j in range((i * 4), ((i * 4) + 4)):
                
                temp = processorTime[i] + tasks[j]
                min_time = max(min_time, temp)
        
        return min_time