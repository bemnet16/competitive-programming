class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        
        total = 0
        answer = 0
        
        for index,value in enumerate(flips):
            
            # summation of each elements
            total += value
            # summation of indices up to this point
            temp = ((index + 1) * (index + 2)) // 2

            # if total and temp is the same it means all numbers are present up to this index
            if total == temp:
                answer += 1
        
        return answer
            