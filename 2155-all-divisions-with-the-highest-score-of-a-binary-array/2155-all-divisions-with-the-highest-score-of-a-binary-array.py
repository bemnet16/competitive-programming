from collections import defaultdict

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        
        count_1 = 0
        
        for num in nums:
            if num == 1:
                count_1 += 1
        
        scores = defaultdict(list)
        scores[count_1].append(0)
        max_score = count_1
        count_0 = 0
        
        for i,num in enumerate(nums):
            
            count_0 += int(num == 0)
            count_1 -= int(num == 1)
            
            score = count_0 + count_1

            scores[score].append(i + 1)
            max_score = max(max_score, score)
        
        
        return scores[max_score]
            
            
            
            
        
        
            
            
            
            
            
            
            
            
            
        