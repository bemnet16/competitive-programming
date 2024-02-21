class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        if left == right: return left
        
        count = 0
        while left != right:
            
            left = left >> 1
            right = right >> 1
            count += 1

        answer = right * (2 ** count)
        # answer = right << count
        
        return answer