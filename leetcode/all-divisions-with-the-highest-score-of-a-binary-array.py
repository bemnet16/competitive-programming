class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        prefix_sum0 = [0]
        prefix_sum1 = [0]
        
        accumulator_0 = 0
        accumulator_1 = 0
        
        for i in range(n):
            
            if nums[i] == 0:
                accumulator_0 += 1
            
            else:
                accumulator_1 += 1
            
            prefix_sum0.append(accumulator_0)
            prefix_sum1.append(accumulator_1)
        
        res = []
        for i in range(n + 1):
            
            left_0 = 0
            right_1 = 0
            
            if i == 0:
                right_1 = prefix_sum1[-1]
            elif i == n:
                left_0 = prefix_sum0[-1]
            else:
                left_0 = prefix_sum0[i]
                right_1 = prefix_sum1[-1] - prefix_sum1[i]
                
            sum_0_1 = left_0 + right_1
            
            res.append([i, sum_0_1])
        
        res.sort(key=lambda x:x[1], reverse=True)
        
        answer = []
        cur = res[0][1]
        
        for i in range(len(res)):
            if res[i][1] == cur:
                answer.append(res[i][0])
            else:
                break
        
        return answer
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        