class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        change_5 = 0
        change_10 = 0
        
        for bill in bills:
            
            # collect '$5'. no need to give a change 
            if bill == 5:
                change_5 += 5
                
            # collect '$10' and give a change '$5'
            elif bill == 10 and change_5:
                change_5 -= 5
                change_10 += 10
            
            # if there is '$10' and '$5' give it and take '$20'
            elif bill == 20 and change_10 and change_5:
                change_10 -= 10
                change_5 -= 5
            
            # otherwise if there is $15 each '$5' give it
            elif bill == 20 and change_5 >= 15:
                change_5 -= 15
            
            # after all we can't make any change. there is no $ to give as a change
            else:
                return False
                
        
        return True
        