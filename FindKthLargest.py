class Solution(object):
    def kthLargestNumber(self, nums, k):
       
       new = []   
       for i in nums:
           new.append(int(i))
       new.sort()
       return str(new[-k])
