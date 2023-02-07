class Solution:
  def isPowerOfThree(self, n: int) -> bool:
    
    isPower = False
        if n > 0:
           isPower = ((3 ** 19) % n == 0)
                
        return isPower

    return n > 0 and 3**19 % n == 0

    #class Solution(object):
    # def isPowerOfThree(self, n):
    #     if  n < 1:
    #         return False
    #     elif n == 1:
    #         return True
    #     else:
    #         return self.isPowerOfThree(n/3)
        
        # i = 1
        # while i <= n:
        #     if i == n:
        #         return True
        #       i *= 3
        # return False
