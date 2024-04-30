class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        pre_xor = [0]
        
        for i in arr:
            pre_xor.append(i ^ pre_xor[-1])
        
        
        answer = []
        
        for left, right in queries:
            
            cur = pre_xor[right + 1] ^ pre_xor[left]
            answer.append(cur)
        
        
        return answer
        