class Solution(object):
    def average(self, salary):
        mx=mi=salary[0]
        tot=0
        for i in salary:
            tot+=i
            if i>mx: mx=i
            elif i<mi: mi=i
        return float(tot-(mi+mx))/(len(salary)-2)