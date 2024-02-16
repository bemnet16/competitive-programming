class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        stack = []
        
        for operation in logs:
            
            if operation == "../" and len(stack) > 0:
                stack.pop()
                
            elif operation != "../" and operation != "./":
                stack.append(operation)
        
        return len(stack)
        