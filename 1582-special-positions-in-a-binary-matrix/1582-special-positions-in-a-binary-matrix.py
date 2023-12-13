class Solution(object):
    def numSpecial(self, mat):
        r=set()
        c=set()
        res = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    if i in r or j in c:
                        continue
                    r.add(i)
                    c.add(j)
                    t=0
                    for k in range(len(mat)):
                        if mat[k][j] == 1:
                            t+=1
                    for l in range(len(mat[0])):
                        if mat[i][l] == 1:
                            t+=1
                    if t == 2:
                        res+=1
        return res
                    
                        