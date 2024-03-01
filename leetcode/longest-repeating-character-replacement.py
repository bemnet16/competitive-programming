class Solution(object):
    def characterReplacement(self, s, k):
        maxlen=0
        left=0
        d={}
        for right in range(len(s)):
            # if s[right] in d:
            #     d[s[right]]+=1
            # else:
            #     d[s[right]]=1
            d[s[right]] = 1 + d.get(s[right],0)
            if (right-left+1) - max(d.values()) > k:
                d[s[left]]-=1
                left+=1
            maxlen=max(maxlen,(right-left+1))
        
        return maxlen