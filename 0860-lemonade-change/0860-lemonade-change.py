class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        ch5 = 0
        ch10 = 0
        ch20 = 0
        
        for bill in bills:
            
            if bill == 5:
                ch5 += 5
                
            elif bill == 10 and ch5:
                ch5 -= 5
                ch10 += 10
            
            elif bill == 20 and ch10 and ch5:
                ch20 += 20
                ch10 -= 10
                ch5 -= 5
            
            elif bill == 20 and ch5 >= 15:
                ch20 += 20
                ch5 -= 15
            
            else:
                return False
                
        
        return True
        