class Solution:
    def minOperations(self, s: str) -> int:
        
        start_0 = ['01'] * (len(s) // 2)
        if len(s) % 2:
            start_0.append('0')
        
        start_0 = ''.join(start_0)
        

        start_1 = ['10'] * (len(s) // 2)
        if len(s) % 2:
            start_1.append('1')
        
        start_1 = ''.join(start_1)
        
        
        diff_1 = bin(int(s, 2) ^ int(start_0, 2)).count('1')
        diff_2 = bin(int(s, 2) ^ int(start_1, 2)).count('1')
        
        return min(diff_1, diff_2)
        