class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        GRAPH = defaultdict(set)
        
        for course, preReq in prerequisites:
            GRAPH[course].add(preReq)
            
        colors = [0 for _ in range(numCourses)]
        
        def dfs(node):
            
            colors[node] = 1
            
            if node in GRAPH:
                for neighbour in GRAPH[node]:
                    if colors[neighbour] == 1:
                        return False
                    if colors[neighbour] == 0:
                        if not dfs(neighbour):
                            return False
            
            colors[node] = 2
            return True
        
        
        for course in GRAPH:
            if colors[course] == 0:
                if not dfs(course):
                    return False
        return True
