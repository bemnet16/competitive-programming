class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        
        graph = defaultdict(set)
        inDegree = [0] * (n)
        
        
        for prevCourse, nextCourse in relations:
            
            prevCourse -= 1
            nextCourse -= 1
            
            inDegree[nextCourse] += 1
            graph[prevCourse].add(nextCourse)
            
        
        
        
        queue = deque()
        maxTime = [0] * (n)
        
        for i, deg in enumerate(inDegree):
            if deg == 0:
                queue.append(i)
                maxTime[i] = time[i]
        
        while queue:
            
            for _ in range(len(queue)):
                
                prevCourse = queue.popleft()
                
                for nextCourse in graph[prevCourse]:
                    
                    inDegree[nextCourse] -= 1
                    maxTime[nextCourse] = max(maxTime[nextCourse], (maxTime[prevCourse] + time[nextCourse]))
                    
                    if inDegree[nextCourse] == 0:
                        queue.append(nextCourse)
        
        
        return max(maxTime)
            
            