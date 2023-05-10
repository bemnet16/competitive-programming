class Solution(object):
    def spiralOrder(self, matrix):
        l,b=0,len(matrix)
        t,r=0,len(matrix[0])
        res=[]
        while l<r and t<b:
            i=l
            while i<r:
                res.append(matrix[t][i])
                i+=1
            t+=1
            j=t
            while j<b:
                res.append(matrix[j][r-1])
                j+=1
            r-=1
            i=r-1
            if not(l<r and t<b):
                break
            while i>=l:
                res.append(matrix[b-1][i])
                i-=1
            b-=1
            j=b-1
            while j>=t:
                res.append(matrix[j][l])
                j-=1
            l+=1
        return res
