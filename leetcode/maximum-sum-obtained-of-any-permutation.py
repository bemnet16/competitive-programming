class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        prefix = [0] * (len(nums) + 1)
        
        for start,end in requests:
            prefix[start] += 1
            prefix[end + 1] -= 1
        
        prefix.pop()
        prefix = list(accumulate(prefix))
        prefix.sort(reverse = True)
        nums.sort(reverse = True)
        print(prefix, nums)
        
        answer = 0
        for i in range(len(nums)):
            if prefix[i] == 0:
                break
            
            temp = prefix[i] * nums[i]
            answer += temp
        
        return answer % (10**9 + 7)
        