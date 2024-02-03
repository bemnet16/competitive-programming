class Solution(object):
    def findMinimumOperations(self, s1, s2, s3):
        res = 0
        pre = 0
        lg = min(len(s1),len(s2),len(s3))
        for i in range(lg):
            if s1[i] == s2[i] and s2[i] == s3[i]:
                pre += 1
            else:
                break
        
        if pre == 0:
            return -1
        
        res = (len(s1) - pre) + (len(s2) - pre) + (len(s3) - pre)
        
        return res
        