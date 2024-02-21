class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        if left == right: return left
        
#         count = 0
#         while left != right:
            
#             left = left >> 1
#             right = right >> 1
#             count += 1

#         answer = right * (2 ** count)
#         # answer = right << count
        
#         return answer

        
        left_bits = bin(left)[2:]
        right_bits = bin(right)[2:]
        
        if len(left_bits) != len(right_bits):
            return 0
        
        answer = 0
        i = 0
        
        while left_bits[i] == right_bits[i]:
            answer += ((2 ** (len(left_bits) - 1 - i)) * (int(left_bits[i])))
            i += 1
        
        return answer