class Solution:
    def __init__(self):
        self.dic = {}
        self.ans = []
        self.n = 0
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.n = len(graph)
        for i in range(self.n): self.dic[i]=graph[i]
        if self.dic[0]:
            self.my_func([], 0)
            return self.ans
        else: return []
    def my_func(self, root, i):
        if i==self.n-1:
            self.ans.append(root+[i])
        elif self.dic[i]:
            for j in self.dic[i]:
                self.my_func(root+[i], j)