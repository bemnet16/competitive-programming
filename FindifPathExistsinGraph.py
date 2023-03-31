class Solution(object):
    def validPath(self, n, edges, source, destination):
        
        def formater(edgs):
            graph = {}
            for i in edgs:
                a,b = i[0],i[1]
                if a not in graph: graph[a] = []
                if b not in graph: graph[b] = []
                graph[a].append(b)
                graph[b].append(a)
            return graph
        edges = formater(edges)
        
        stc = [source]
        s = source
        v = []
        while stc:
            cur = stc.pop(0)
            if cur == destination:
                return True
            if cur in v:
                continue
            v.append(cur)
            for i in edges[cur]:
                if i not in v:
                    stc.append(i)
        return False
