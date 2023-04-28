class Solution(object):
    def reverseParentheses(self, s):
        stc=[]
        for i in s:
            if i==')':
                temp=[]
                while stc:
                    cur=stc.pop()
                    if cur=='(':
                        break
                    temp.append(cur)
                stc.extend(temp)
                continue
            stc.append(i)
        return "".join(stc)
