from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        counter = Counter(nums)
        
        answer = []
        q = len(nums)/3
        
        for num, count in counter.items():
            if count > q:
                answer.append(num)
        
        return answer