class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        num_row = 0
        count = defaultdict(int)
        answer = [[]]
        
        for num in nums:
            
            if count[num] >= len(answer):
                answer.append([])
                
            answer[count[num]].append(num)
            count[num] += 1
        
        return answer