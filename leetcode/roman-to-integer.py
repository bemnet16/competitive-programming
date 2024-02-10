class Solution(object):
    def romanToInt(self, s):
        l,t={'IV':-1,'IX':-1,'XL':-10,'XC':-10,'CD':-100,'CM':-100},0
        for i in range(len(s)):
            r=s[i]
            if i<len(s)-1: r=s[i]+s[i+1]
            if r in l.keys(): t+=l[r]
            elif r[0]=='I': t+=1
            elif r[0]=='V': t+=5
            elif r[0]=='X': t+=10
            elif r[0]=='L': t+=50
            elif r[0]=='C': t+=100
            elif r[0]=='D': t+=500
            elif r[0]=='M': t+=1000
        return t
            