class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        times = []
        for time in timePoints:
            hour, mini = map(int, time.split(":"))
            if hour == 0 and mini == 0:
                hour = 24
            
            times.append(hour * 60 + mini)
        
        times.sort()
        
        min_time = 1440 - times[-1] + times[0]
        for i in range(1, len(times)):
            min_time = min(min_time, times[i] - times[i - 1])
        
        return min_time