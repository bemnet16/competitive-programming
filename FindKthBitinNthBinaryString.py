class Solution(object):
    def findKthBit(self, n, k):
        def reverseInvert(s):
            t=""
            for i in s:
                if i=='0': t+='1'
                else: t+='0'
            return t[::-1]
        def kthbit(n):
            if n<=1: return "0"
            return kthbit(n-1)+"1"+reverseInvert(kthbit(n-1))
        return kthbit(n)[k-1]
