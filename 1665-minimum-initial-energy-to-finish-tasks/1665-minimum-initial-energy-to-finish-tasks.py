class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        
        n = len(tasks)
        
        if n == 1:
            return tasks[0][-1]
        
        tasks.sort(key=lambda x: x[0] - x[1])
        
        total = 0
        rem = 0
        
        for actual, mini in tasks:
            
            if mini > rem:
                total += (mini - rem)
                rem = mini
            rem -= actual
            
        return total