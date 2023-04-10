class Solution(object):
    def isValid(self, s):
        stc=[]
        for c in s:
            if c=='(' or c=='[' or c=='{':
                stc.append(c)
            elif c==')' or c==']' or c=='}':
                if not stc: return False
                t=stc.pop()
                if c==')' and t!='(': return False
                elif c==']' and t!='[': return False
                elif c=='}' and t!='{': return False
        return not stc
