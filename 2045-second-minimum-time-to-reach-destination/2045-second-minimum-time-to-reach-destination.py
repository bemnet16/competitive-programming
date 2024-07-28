class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        prev, boundary, count = set(), [1], 0
        while n not in prev:
            next_boundary = [b for a in boundary for b in graph[a] if not b in prev]
            prev.update(boundary)
            boundary = next_boundary
            count += 1
        if n not in boundary:
            count += 1
        
        total_time = 0
        while count:
            count -= 1
            if (total_time // change) % 2 == 1:
                total_time = total_time + change - total_time % change
            total_time += time

        return total_time 