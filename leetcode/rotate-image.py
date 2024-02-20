class Solution(object):
    def rotate(self, matrix):
        r=[]
        for i in range(len(matrix)):
            t=[]
            for j in range(len(matrix)-1,-1,-1):
                t.append(matrix[j][i])
            r.append(t)
            
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j]=r[i][j]
        return matrix