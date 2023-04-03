class Solution(object):
    def longestCommonPrefix(self, strs):
        temp=""
        if len(strs)==1:return strs[0]
        for i in range(min(len(strs[0]),len(strs[1]))):
            if strs[0][i]!=strs[1][i]:
                break
            temp+=strs[0][i]
        if temp == "":return temp
        for i in strs:
            res = ""
            if i.startswith(temp):
                res=temp
                continue
            for j in range(min(len(i),len(temp))):
                if i[j]!=temp[j]:
                    break
                res+=temp[j]
            if res=="":
                return res
            temp=res
        return temp
            
            
            
