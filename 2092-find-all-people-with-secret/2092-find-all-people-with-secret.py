from collections import deque

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        
        graph = defaultdict(set)
        knowSecret = [float("inf")] * n
        knowSecret[0], knowSecret[firstPerson] = 0, 0
        
        for x, y, t in meetings:
            graph[x].add((y, t))
            graph[y].add((x, t))
            
        queue = deque([(0,0), (firstPerson, 0)])
        
        while queue:
            
            for _ in range(len(queue)):
                
                person, time = queue.popleft()
                
                for nextPerson, nextTime in graph[person]:
                    
                    if nextTime >= time and knowSecret[nextPerson] > nextTime:
                        knowSecret[nextPerson] = nextTime
                        queue.append((nextPerson, nextTime))
        
        
        answer = []
        for i, secret in enumerate(knowSecret):
            if secret != float("inf"):
                answer.append(i)
        
        
        return answer