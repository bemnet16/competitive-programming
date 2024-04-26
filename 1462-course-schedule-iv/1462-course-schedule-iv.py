from collections import deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        
        outDegree = [0] * numCourses
        adjGraph = defaultdict(set)
        preRequests = defaultdict(set)
        
        for a, b in prerequisites:
            outDegree[b] += 1
            adjGraph[a].add(b)
            
        
        queue = deque()
        
        for i, degree in enumerate(outDegree):
            if degree == 0:
                queue.append(i)
                outDegree[i] -= 1
        
        
        while queue:
            
            for _ in range(len(queue)):
                
                preCourse = queue.popleft()
                
                for course in adjGraph[preCourse]:
                    
                    outDegree[course] -= 1
                    
                    if outDegree[course] == 0:
                        queue.append(course)
                    
                    if preCourse not in preRequests[course]:
                        preRequests[course].add(preCourse)
                        preRequests[course].update(preRequests[preCourse])
                        
        
        answer = []
        
        for a, b in queries:
            if a in preRequests[b]:
                answer.append(True)
            else:
                answer.append(False)
        
        
        return answer
        
