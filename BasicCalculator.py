class Solution(object):
    def calculate(self, s):   ### Is works for all four operation {"+","-","*","/"}
        def strSum(s):
            stc=[]
            c,p,t='','+',0
            for i in range(len(s)):
                if s[i].isdigit():
                    if c=='':
                        t=t*10+int(s[i])
                if s[i] in '+-*/' or i==len(s)-1:
                    c,p=p,s[i]
                    if c=='+': stc.append(t)
                    elif c=='-': stc.append(-t)
                    elif c=='*': stc.append(stc.pop()*t)
                    elif c=='/':
                        cur=stc.pop()
                        if cur<0: stc.append(-(abs(cur)/t))
                        else: stc.append(cur/t)
                    t=0
                    c=''
            return sum(stc)
        stc=[]
        for i in s:
            if i==' ': continue
            if i==')':
                t=""
                cur=stc.pop()
                while cur!='(':
                    t=cur+t
                    cur=stc.pop()
                su=strSum(str(t))
                if stc and stc[-1]=='-' and su<0:
                    stc.pop()
                    stc.append('+')
                    stc.append(str(-1*su))
                    continue
                stc.append(str(su))
            else:
                stc.append(i)
                
        return strSum("".join(stc))
        
