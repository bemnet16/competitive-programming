class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stack = [""]
        temp = ""
        
        for char in s:
            if char == '(':
                if temp:
                    stack.append(temp)
                    temp = ""
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    temp = stack.pop() + temp
                stack.pop()
                stack.append(temp[::-1])
                temp = ""
            else:
                temp += char
        
        stack.append(temp)
        return "".join(stack)