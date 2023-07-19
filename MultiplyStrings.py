class Solution(object):
    def multiply(self, num1, num2):
        num={}
        for i in range(10):
            num[str(i)]=i
        n1=0
        for i in range(len(num1)):
            n1=n1*10+num[num1[i]]
        n2=0
        for j in range(len(num2)):
            n2=n2*10+num[num2[j]]
        return str(n1*n2)
