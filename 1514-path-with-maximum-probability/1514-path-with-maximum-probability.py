class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = {}

        for i,(p,q) in enumerate(edges):
            if p not in graph:
                graph[p] = {}
            if q not in graph:
                graph[q] = {}  
            graph[p][q] = succProb[i]
            graph[q][p] = succProb[i]
        
        memo = {}
        que = deque([[start,1]])
        answer = 0
        while que:
            node,prob = que.popleft()
            if node == end:
                answer = max(answer,prob)
            if node in memo and memo[node] >= prob:
                continue
            memo[node] = prob
            if node not in graph:
                continue
            for nei,p in graph[node].items():
                que.append([nei,prob*p])
        return answer