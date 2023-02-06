class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        for i,num in enumerate(nums):
            nums[i]=str(num)

        def check(n1,n2):
            if n1+n2 > n2+n1:
                return -1
            else:
                return 1

        nums= sorted(nums,key=cmp_to_key(check))

        return str(int(''.join(nums)))
