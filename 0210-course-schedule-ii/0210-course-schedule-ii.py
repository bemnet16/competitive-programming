from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        deg = defaultdict(int)
        grp = defaultdict(set)
        
        
        for a, b in prerequisites:
            grp[b].add(a)
            deg[a] += 1
            if not deg[b]:
                deg[b] = 0
        
        for i in range(numCourses):
            if not i in deg:
                deg[i] = 0
                grp[i] = {}
        
        queue = deque()
        visited = set()
        
        for node in deg:
            if deg[node] == 0:
                queue.append(node)
                visited.add(node)
        
        answer = []
        while queue:
            
            for i in range(len(queue)):
                
                node = queue.popleft()
                answer.append(node)
                
                for nei in grp[node]:
                    if nei not in visited:
                        if deg[nei] == 1:
                            queue.append(nei)
                            deg[nei] = 0
                            visited.add(nei)
                        else:
                            deg[nei] -= 1
        
        
        if len(answer) == numCourses:
            return answer
        return []