class Solution(object):
    def reverseString(self, s):
        
        
        def reverse(l, r, d, s):
            
            if d == 0:
                return s
            
            s[l], s[r] = s[r], s[l]
            
            return reverse(l + 1, r - 1, d - 1, s)
        
        return reverse(0, len(s) - 1, len(s)//2, s)
        
        
#         for i in range(len(s) // 2):
#             s[i], s[-i - 1] = s[-i - 1], s[i]
        
#         return s