class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        n = len(arr)
        
        # record the smaller value span of each number /till where is it small value to the right/ 
        next_span = {}
        next_stack = []
        
        # record the span until which it is smaller to the left
        previous_span = {}
        prev_stack = []
        
        for i in range(n):
            
            # record the span length of each num until where is it smallest to the right start from itself
            ### using non-decreasing monotonic stack ###
            while next_stack and arr[next_stack[-1]] > arr[i]:
                popped = next_stack.pop()
                next_span[popped][1] = i
            
            next_stack.append(i)
            next_span[i] = [i, n]
            
            
            # record the span length of each element till where is it smaller to the left start from its index
            ### using strictly increasing monotonic stack ###
            while prev_stack and arr[prev_stack[-1]] >= arr[n - 1 - i]:
                popped = prev_stack.pop()
                previous_span[popped][1] = (n - 1 - i)
            
            prev_stack.append(n - 1 - i)
            previous_span[n - 1 - i] = [n - 1 - i, -1]
        
        
        
        answer = 0
        for i,v in enumerate(arr):
            
            left = previous_span[i][0] - previous_span[i][1]
            right = next_span[i][1] - next_span[i][0]
            
            answer += (left * right * v)
        
        return answer % (10 ** 9 + 7)
            