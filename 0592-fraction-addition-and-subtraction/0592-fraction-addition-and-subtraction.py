class Solution:
    def fractionAddition(self, expression: str) -> str:
        
        def gcd(a, b):
            if a % b == 0:
                return b
            return gcd(b, a % b)
        
        i = 5
        if expression[0] != '-':
            expression = '+' + expression
            
        ans = [expression[:2], 0]
        
        if expression[2] == '0':
            ans[0] = expression[:3]
            i += 1
            if 5 < len(expression) and expression[5] == '0':
                ans[1] = expression[4:6]
                i += 1
            else:
                ans[1] = int(expression[4])
        elif 4 < len(expression) and expression[4] == '0':
            ans[1] = expression[3:5]
            i += 1
        else:
            ans[1] = expression[3]
        
        
        while i < len(expression):
            
            operation = expression[i - 1]
            
            if expression[i + 1] == '0':
                numerator = int(expression[i:i + 2])
                i += 1
            else:
                numerator = int(expression[i])
            
            
            if i + 3 < len(expression) and expression[i + 3] == '0':
                denominator = int(expression[i + 2: i + 4])
                i += 1
            else:
                denominator = int(expression[i + 2])
                
                
            common_den = int(ans[1]) * denominator
            
            if operation == '-':
                ans[0] = (int(ans[0]) * (common_den // int(ans[1]))) - (numerator * (common_den // denominator))
            
            else:
                ans[0] = (int(ans[0])* (common_den // int(ans[1]))) + (numerator * (common_den // denominator))
            
            divisor = gcd(abs(ans[0]), common_den)
            ans[0] = str(ans[0] // divisor)
            ans[1] = str(common_den // divisor)
            
            
            i += 4
        
        
        ans[0] = str(int(ans[0]))
        return "/".join(ans)
        
        