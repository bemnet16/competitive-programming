class Solution(object):
    def removeKdigits(self, num, k):
        if len(num)==k:
            return "0"
        stc=[]
        for i in num:
            while k and stc and stc[-1]>i:
                stc.pop()
                k-=1
            stc.append(i)
        if k:
            return str(int("".join(stc[:-k])))
        return str(int("".join(stc)))
