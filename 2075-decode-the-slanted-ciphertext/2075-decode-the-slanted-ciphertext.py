class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        
        n = len(encodedText)
        
        # calculate the number of cols will we have
        cols = len(encodedText) // rows
        
        # create empty matrix that hold our cipher text later
        matrix = [[' ' for _ in range(cols)] for _ in range(rows)]
        
        # 'k' - index for the encodedText
        k = 0
        
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = encodedText[k]
                k += 1
                
        
        answer = []
        
        for i in range(cols):
            
            k = i
            isEnd = False
            
            for j in range(rows):
                
                if k >= cols:
                    isEnd = True
                    break
                    
                answer.append(matrix[j][k])
                k += 1
                
            if isEnd:
                break
                
                
        # remove all spaces from the right
        while answer and answer[-1] == " ":
            answer.pop()
        
        return "".join(answer)