class Solution(object):
    def numIdenticalPairs(self, nums):
        
        answer = 0
        count_save = defaultdict(int)
        for num in nums:
            count_save[num] += 1
            
        for num in count_save:
            count = count_save[num]
            count = (count * (count - 1)) // 2
            answer += count
        
        return answer