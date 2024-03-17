class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if not intervals:
            return [newInterval]
        
        
        low = 0 
        high = len(intervals) - 1
        
        while low <= high:
            
            mid = low + (high - low) // 2
            
            start, end = intervals[mid]
            
            if start > newInterval[0]:
                high = mid - 1
            
            else:
                low = mid + 1
        
        
        
        intervals.insert(low, newInterval)
        
        
        mergedInterval = []
        
        for interval in intervals:
            
            if not mergedInterval or mergedInterval[-1][1] < interval[0]:
                mergedInterval.append(interval)
                
            else:
                mergedInterval[-1][1] = max(mergedInterval[-1][1], interval[1])
                
                
        return mergedInterval
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            