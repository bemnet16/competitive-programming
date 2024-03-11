class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        answer = []
        s_set = defaultdict(int)
        
        for char in s:
            s_set[char] += 1
        
        
        for char in order:
            
            if s_set[char] > 0:
                answer.append(char * s_set[char])
                del s_set[char]
        
        
        for k in s_set:
            answer.append(k * s_set[k])
        
        
        
        return "".join(answer)
        