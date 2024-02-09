class NumArray(object):

    def __init__(self, nums):
        self.p_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.p_sum[i + 1] = self.p_sum[i] + nums[i]

    def sumRange(self, left, right):
        return self.p_sum[right + 1] - self.p_sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)