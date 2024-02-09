class Solution(object):
    def longestCommonPrefix(self, strs):
        
        st = strs[0]
        answer = []
        
        for i in range(len(st)):
            for word in strs:
                if i >= len(word) or st[i] != word[i]:
                    return "".join(answer)
            answer.append(st[i])
        
        return "".join(answer)