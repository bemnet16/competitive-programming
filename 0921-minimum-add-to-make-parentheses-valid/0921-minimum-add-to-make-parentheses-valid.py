class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        stack = []
        answer = 0

        for parentheses in s:
            if parentheses == '(':
                stack.append(parentheses)

            elif parentheses == ')':
                if not stack:
                    answer += 1
                else:
                    stack.pop()
        
        # add the remaining openning parentheses
        answer += len(stack)

        return answer