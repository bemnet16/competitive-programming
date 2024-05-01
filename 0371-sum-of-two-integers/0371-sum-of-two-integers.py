class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        while b & 0xffffffff > 0:
            temp = (a & b) << 1
            a = a ^ b
            b = temp
        
        return a & 0xffffffff if b > 0 else a
        
        
#         r = 0
#         temp_ans = 1
        
#         while a or b or r:
            
#             c = 0
            
#             if (1 & a & b) or (r & (a ^ b)):
#                 c = 1
            
#             temp = r ^ a ^ b
            
#             temp_ans = (temp_ans << 1) ^ (temp & 1)
            
#             a = a >> 1
#             b = b >> 1
#             r = c
        
            
#         ans = 0
#         while temp_ans:
            
#             ans = (ans << 1) ^ (temp_ans & 1)
#             temp_ans = temp_ans >> 1
        
        
#         ans = ans >> 1
#         return ans
        