class Solution(object):
    def kthLargestNumber(self, nums, k):
        
        return str(sorted(list(map(int, nums)))[-k])