class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        answer = [-1 for i in range(len(intervals))]
        
        for i, interval in enumerate(intervals):
            interval.append(i)
            
        intervals.sort(key=lambda x:x[0])
        
        for starti, endi, indexi in intervals:
            
            low = 0
            high = len(intervals) - 1
            
            while low <= high:
                
                mid = low + (high - low) // 2
                startj, endj, indexj = intervals[mid]
                
                if startj < endi:
                    low = mid + 1
                
                else:
                    high = mid - 1
                    
            
            if low < len(intervals):
                answer[indexi] = intervals[low][2]
        
        
        return answer
        