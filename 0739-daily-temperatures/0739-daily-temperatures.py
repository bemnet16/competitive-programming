class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        answer = [0] * n
        mono_stack = []
        
        for i in range(n):
            
            while mono_stack and temperatures[mono_stack[-1]] < temperatures[i]:
                popped_item = mono_stack.pop()
                answer[popped_item] = (i - popped_item)
                
            mono_stack.append(i)
        
        return answer