class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        
        res=[]
        for num in nums:
            temp=0
            for n in nums:
                if n<num:
                    temp+=1
            res.append(temp)
        return res