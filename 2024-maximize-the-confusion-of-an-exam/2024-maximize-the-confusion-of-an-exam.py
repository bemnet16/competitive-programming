class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        num_true=0
        num_false=0
        left_idx=0
        answer=0
        
        
        for right_idx in range(len(answerKey)):
            
            if answerKey[right_idx] == "T":
                num_true += 1
                
            else:
                num_false += 1
                
                
            if num_true > k and num_false > k:
                
                if answerKey[left_idx] == "T":
                    num_true -= 1
                    
                else:
                    num_false -= 1
                left_idx += 1
                
                
            answer = max(answer,(right_idx - left_idx + 1))
        
        
        
        return answer
            
        