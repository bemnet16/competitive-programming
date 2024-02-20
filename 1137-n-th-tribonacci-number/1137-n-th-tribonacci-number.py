class Solution:
    def tribonacci(self, n: int) -> int:
        t0,t1,t2=0,1,1
        t=[0,1,1]
        for i in range(3,38):
            t.append(t[i-3]+t[i-2]+t[i-1])
        return t[n]