from collections import deque

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        graph = defaultdict(set)
        for i, v in enumerate(manager):
            if i == headID:
                continue
            
            graph[v].add(i)
        
        
        queue = deque([(headID, informTime[headID])])
        time_need = 0
        
        while queue:
            
            cur_head, cur_time = queue.popleft()
            time_need = max(time_need, cur_time)
            
            for nex_head in graph[cur_head]:
                queue.append((nex_head, cur_time + informTime[nex_head]))
        
        
        return time_need
            
            
        