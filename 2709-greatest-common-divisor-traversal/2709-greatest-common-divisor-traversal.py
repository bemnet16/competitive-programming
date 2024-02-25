class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        nums = set(nums)
        if 1 in nums:
            return False
        if len(nums) == 1:
            return True

        # approach 2: sort from high to low, then "propagate the prime factors from big numbers to smaller numbers
        nums = sorted(nums, reverse=True)
        n = len(nums)
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                d = gcd(nums[i], nums[j])
                if d > 1:
                    # replace nums[j] by smallest common multiple of nums[i] and nums[j]
                    nums[j] *= nums[i] // d
                    # then check the next number, we don't need to check nums[i] with other numbers anymore because the "new" nums[j] will take care of that
                    break
            else:
                # this means gcd of nums[i] to all smallere numbers is 1
                return False
        
        return True