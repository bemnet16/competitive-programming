class Solution(object):
    def addSpaces(self, s, spaces):
        po=0
        idx=spaces[po]
        res=[]
        for i,v in enumerate(s):
            if i==idx:
                res.append(" ")
                res.append(v)
                po+=1
                if po<len(spaces):
                    idx=spaces[po]
            else:
                res.append(v)
        return "".join(res)
