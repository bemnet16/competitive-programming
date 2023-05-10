class Solution(object):
    def compress(self, chars):
        res=""
        i=0
        while i<len(chars):
            t=i+1
            j=1
            while t<len(chars) and chars[i]==chars[t]:
                t+=1
                j+=1
            if j>1:
                res+=chars[i]+str(j)
            else:
                res+=chars[i]
            i=t
        chars[:]=list(res)
