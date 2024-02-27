class Solution(object):
    def decodeString(self, s):
        stk=[]
        for v in s:
            if v != "]":
                stk.append(v)
            elif v == "]":
                temp = ""
                j=len(stk) - 1
                while j >= 0 and stk[j] != "[":
                    temp = stk.pop() + temp
                    j-=1
                if stk[j] == "[":
                    stk.pop()
                    num=""
                    while stk and stk[-1].isdigit():
                        num=stk.pop() + num
                    stk.append(int(num)*temp)
                    
        return "".join(stk)