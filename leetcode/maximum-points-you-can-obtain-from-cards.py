class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        max_score = 0
        cur_score = 0
        
        for i in range(k):
            
            cur_score += cardPoints[i]
        
        
        max_score = cur_score
        
        
        for i in range((k - 1), -1, -1):
            
            cur_score += (-cardPoints[i] + cardPoints[i - k])
            
            max_score = max(max_score, cur_score)
        
        
        
        
        return max_score
        