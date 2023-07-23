class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        
        res=[]
        for num in nums:
            co=0
            for o_num in nums:
                if o_num<num:
                    co+=1
            res.append(co)
        return res
