class Solution(object):
    def calculate(self, s):
        stc=[]
        c,p,t='','+',0
        for i in s:
            if i.isdigit():
                if c=='':
                    t=t*10+int(i)
            elif i in '+-*/':
                c,p=p,i
                if c=='+': stc.append(t)
                elif c=='-': stc.append(-t)
                elif c=='*': stc.append(stc.pop()*t)
                elif c=='/':
                    cur=stc.pop()
                    if cur<0: stc.append(-(abs(cur)/t))
                    else: stc.append(cur/t)
                t=0
                c=''
        c=p
        if c=='+': stc.append(t)
        elif c=='-': stc.append(-t)
        elif c=='*': stc.append(stc.pop()*t)
        elif c=='/':
            cur=stc.pop()
            if cur<0: stc.append(-(abs(cur)/t))
            else: stc.append(cur/t)
                
        return sum(stc)
