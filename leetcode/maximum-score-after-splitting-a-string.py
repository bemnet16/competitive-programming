class Solution:
    def maxScore(self, s: str) -> int:
        length = len(s)
        prefix_0 = [0] * length
        prefix_1 = [0] * length
        answer = 0
        
        sum_0 = 0
        sum_1 = 0
        
        for i in range(length):
            if s[i] == '0':
                sum_0 += 1
            else:
                sum_1 += 1
            
            prefix_0[i] += sum_0
            prefix_1[i] += sum_1
        
        for i in range(1,length):
            score = (prefix_1[-1] - prefix_1[i - 1]) + (prefix_0[i - 1])
            answer = max(score, answer)
        
        return answer
            