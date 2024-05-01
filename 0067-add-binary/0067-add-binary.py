class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        return bin(int(a, 2) + int(b, 2))[2:]
        
        
        # if len(a) < len(b):
        #     a="0"*(len(b)-len(a)) + a
        # elif len(a) > len(b):
        #     b="0"*(len(a)-len(b)) + b
        # r=0
        # s=""
        # for i in range(len(a)-1,-1,-1):
        #     s+=str((int(a[i])+int(b[i])+r)%2)
        #     r=(int(a[i])+int(b[i])+r)//2
        # if r!=0: s+=str(r)
        # s=s[::-1]
        # return s
        