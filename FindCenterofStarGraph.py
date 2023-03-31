class Solution(object):
    def findCenter(self, edges):
        a,b = edges[0][0],edges[0][1]
        x,c="",""
        for i in edges:
            if not(a in i or b in i):
                break
            if x!="a" and a in i:
                x=a
            elif a not in i:
                x="a"
            if c!="b" and b in i:
                c=b
            elif b not in i:
                c="b"
        if type(x)==int:
            return x
        return c
                
            
                
            
            
