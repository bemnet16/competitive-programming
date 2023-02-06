class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        op_count = 0
        temp = {}
        for x in nums:
            j = k - x
            if j in temp and temp[j] > 0:
                op_count += 1
                temp[j] -= 1
            else:
                if x not in temp:
                    temp[x] = 0
                temp[x] += 1

        return op_count
