class Solution(object):
    def findKthLargest(self, nums, k):
        
        heapify(nums)
        return nlargest(k, nums)[-1]
