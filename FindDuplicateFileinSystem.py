class Solution(object):
    def findDuplicate(self, paths):
        d={}
        for path in paths:
            pa = path.split(" ")
            root=pa[0]
            for i in range(1,len(pa)):
                fi,con=pa[i].split("(")
                if con not in d:
                    d[con]=[root + "/" + fi]
                else:
                    d[con].append(root + "/" + fi)
        res=[]
        for p in d:
            if len(d[p])>1:
                res.append(d[p])
        return res
