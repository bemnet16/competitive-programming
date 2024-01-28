class Solution(object):
    def kWeakestRows(self, mat, k):
        res = []
        for i in range(len(mat)):
            ones = mat[i].count(1)
            mat[i] = ([ones,i])
        
        mat.sort(key=lambda x:(x[0], x[1]))
        
        for i in range(k):
            res.append(mat[i][1])
        
        return res