class Solution:
    def largestInteger(self, num: int) -> int:
        
        odd = []
        even = []
        
        for n in str(num):
            if int(n) % 2 == 0:
                even.append(int(n))
            else:
                odd.append(int(n))
        
        odd.sort()
        even.sort()
        
        answer = 0
        
        for n in str(num):
            if int(n) % 2 == 0:
                answer = answer * 10 + even.pop()
            else:
                answer = (answer * 10) + odd.pop()
            
        return answer
        