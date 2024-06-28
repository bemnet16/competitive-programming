class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        
        degree = defaultdict(int)
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
        
        
        ans = 0
        for deg in sorted(degree.values(), reverse=True):
            ans += deg * n
            n -= 1
        
        return ans