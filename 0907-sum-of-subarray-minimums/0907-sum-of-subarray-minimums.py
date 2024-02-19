class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        prefix = {}
        stk = []
        
        for i in range(len(arr)):
            while stk and arr[stk[-1]] > arr[i]:
                popped = stk.pop()
                prefix[popped][1] = i
            
            stk.append(i)
            prefix[i] = [i, len(arr)]
        
        suffix = {}
        stack = []
        
        for i in range(len(arr) - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                popped = stack.pop()
                suffix[popped][1] = i
            
            stack.append(i)
            suffix[i] = [i, -1]
        
        answer = 0
        for i,v in enumerate(arr):
            
            left = suffix[i][0] - suffix[i][1]
            right = prefix[i][1] - prefix[i][0]
            
            answer += (left * right * v)
        
        return answer % (10 ** 9 + 7)
            