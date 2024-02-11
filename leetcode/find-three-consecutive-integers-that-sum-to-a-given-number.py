class Solution(object):
    def sumOfThree(self, num):
        
        reminder = num % 3
        
        # If it's not divisible by 3 it can't be reprsented by sum of consecutive integers
        if reminder != 0:
            return []
        
        # ((x - 1) + (x) + (x + 1)) = num => 3x = num => num / 3 = x 
        quotient = num / 3
        
        num_1 = quotient - 1
        num_2 = quotient 
        num_3 = quotient + 1
        
        return [num_1, num_2, num_3]