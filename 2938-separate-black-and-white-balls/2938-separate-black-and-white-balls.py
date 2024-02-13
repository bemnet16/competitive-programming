class Solution:
    def minimumSteps(self, s: str) -> int:
        
        answer = 0
        suffix_sum = 0
        
        for i in range((len(s) - 1), -1, -1):
            
            # count the number of '0's 
            if s[i] == '0':
                suffix_sum += 1
            
            # every '1' should be swapped with every '0' on its right side
            else:
                answer += suffix_sum
            
        return answer
        