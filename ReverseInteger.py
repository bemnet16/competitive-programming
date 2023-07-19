class Solution(object):
    def reverse(self, x):
        ip=x>=0
        r=0
        if not ip:x=0-x
        while x>0:
            re=x%10
            r=r*10+re
            x=x//10
        if r<-2**31 or r>2**31-1:
            return 0
        if ip:
            return r
        r*=-1
        return r 
