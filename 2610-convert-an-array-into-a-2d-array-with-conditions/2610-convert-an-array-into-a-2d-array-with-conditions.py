class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        num_row = 0
        counter = defaultdict(int)
        
        for num in nums:
            counter[num] += 1
            num_row = max(num_row, counter[num])
        
        
        answer = [[] for _ in range(num_row)]
        
        for num in counter:
            for count in range(counter[num]):
                answer[count].append(num)
        
        return answer