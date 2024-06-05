class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        answer = []
        
        for op in operations:
            
            if op == "C":
                answer.pop()
            
            elif op == "D":
                answer.append(answer[-1] * 2)
            
            elif op == "+":
                answer.append(answer[-2] + answer[-1])
            
            else:
                answer.append(int(op))
        
        
        return sum(answer)
        