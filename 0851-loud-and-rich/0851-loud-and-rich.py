from collections import deque

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        degreeCount = [0] * len(quiet)
        graph = defaultdict(set)
        minQuiet = defaultdict(list)

        for i, q in enumerate(quiet):
            heappush(minQuiet[i], [-q, i])
        
        for a, b in richer:
            degreeCount[b] += 1
            graph[a].add(b)
        
        
        queue = deque()
        visited = set()
        
        for i, degree in enumerate(degreeCount):
            if degree == 0:
                queue.append(i)
                visited.add(i)
        

        
        answer = list(range(len(quiet)))
        
        while queue:
            
            for _ in range(len(queue)):
                
                node = queue.popleft()
                answer[node] = minQuiet[node][0][1]
                
                for neighbor in graph[node]:
                    
                    if neighbor not in visited:

                        if degreeCount[neighbor] == 1:
                            queue.append(neighbor)
                            visited.add(neighbor)
                            degreeCount[neighbor] = 0

                        else:
                            degreeCount[neighbor] -= 1

                        heappushpop(minQuiet[neighbor], minQuiet[node][0])
        
        
        return answer
