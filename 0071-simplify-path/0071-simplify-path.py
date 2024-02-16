class Solution:
    def simplifyPath(self, path: str) -> str:
        
        directories = path.split("/")
        stack = ["/"]
        
        print(directories)
        
        for d in directories:
         
            if d == '':
                continue
               

            elif d == ".." and len(stack) > 2:
                stack.pop()
                stack.pop()

            elif d != "" and d != ".." and d != ".":
                stack.append(d)
                if stack[-1] != "/":
                     stack.append("/")
            
            print(stack)
        
        if len(stack) > 1 and stack[-1] == "/":
            stack.pop()
        
        return "".join(stack)
            
        