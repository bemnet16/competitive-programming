class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t): return False
        sd,td={},{}
        for i in range(len(s)):
            if s[i] not in sd:
                sd[s[i]]=1
            else:
                sd[s[i]]=sd[s[i]]+1
            if t[i] not in td:
                td[t[i]]=1
            else:
                td[t[i]]=td[t[i]]+1
        if sd==td:
            return True
        return False
            
