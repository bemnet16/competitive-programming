class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        
        graph = defaultdict(set)
        
        for equation, value in zip(equations, values):
            A, B = equation
            graph[A].add((B, value))
            graph[B].add((A, 1/value))
            
        
        track = defaultdict(tuple)
        visited = set()
        
        def dfs(start, end):
            
            if not (start in graph and end in graph):
                return 
            
            visited.add(start)
            
            for nxt, val in graph[start]:
                if nxt not in visited:
                    track[nxt] = (start, val)
                    if nxt == end:
                        return end

                    dfs(nxt, end)
                
                
        def calculate(start, end):
            val = 1
            while end != start:
                if not end in track:
                    return -1
                val *= track[end][1]
                end = track[end][0]
            return val
                
        
        answer = []
        for A, B in queries:
            dfs(A, B)
            if track:
                answer.append(calculate(A, B))
            else:
                answer.append(-1)
            track = defaultdict(set)
            visited = set()
            
        
        return answer
            
            
            