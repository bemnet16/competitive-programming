class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        
        answer = []
        
        shifts[-1] %= 26
        for i in range(len(shifts) - 2, -1, -1):
            shifts[i] = (shifts[i] + shifts[i + 1]) % 26
        

        for i, char in enumerate(s):
            answer.append(chr(97 + ((ord(char) + shifts[i] - 97) % 26)))
        
                          
        return "".join(answer)
        