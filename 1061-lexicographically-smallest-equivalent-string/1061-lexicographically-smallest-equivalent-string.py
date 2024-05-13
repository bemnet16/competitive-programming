class Solution:
    
    def __init__(self):
        self.parent = {chr(i): chr(i) for i in range(97, 123)}
    
    def find(self, x):
            
        while x != self.parent[x]:
            x = self.parent[x]
        return x
    
    
    def union(self, x, y):
            
        rootX, rootY = self.find(x), self.find(y)

        if rootX <= rootY:
            self.parent[rootY] = rootX

        else:
            self.parent[rootX] = rootY


    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        answer = []
        
        for char1, char2 in zip(s1, s2):
            self.union(char1, char2)
        
        for s in baseStr:
            answer.append(self.find(s))
        
        
        return "".join(answer)