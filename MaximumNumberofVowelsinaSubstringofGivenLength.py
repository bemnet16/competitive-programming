class Solution(object):
    def maxVowels(self, s, k):
        tot,count=0,0
        for i in range(len(s)):
            if s[i] in 'aeiou':
                count+=1
            if i>=k and s[i-k] in 'aeiou':
                count-=1
            tot=max(tot,count)
        return tot
