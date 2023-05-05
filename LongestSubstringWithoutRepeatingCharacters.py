class Solution(object):
    def lengthOfLongestSubstring(self, s):
        r,t="",0
        for c in s:
            if c not in r:
                r+=c
                if len(r)>t:t=len(r)
            else:r=r[r.index(c)+1:] + c
        return t
