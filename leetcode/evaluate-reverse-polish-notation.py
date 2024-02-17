class Solution(object):
    def evalRPN(self, tokens):
        stc = []
        for i in tokens:
            if i == '+' or i == '-' or i == '*' or i == '/':
                ro = stc.pop()
                lo = stc.pop()
                if i == '+':
                    temp = lo + ro
                elif i == '-':
                    temp = lo - ro
                elif i == '*':
                    temp = lo * ro
                elif i == '/':
                    temp = int(lo / (ro + 0.0))
                stc.append(temp)
            else:
                stc.append(int(i))
        
        return stc[0]