from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        counter = defaultdict(int)
        
        for num in nums:
            
            counter[num] += 1
            if len(counter) <= 2:
                continue
            
            new_counter = defaultdict(int)
            for n in counter:
                if counter[n] > 1:
                    new_counter[n] = counter[n] - 1
                    
            counter = new_counter
            
        
        answer = []
        for num in counter:
            if nums.count(num) > len(nums) / 3:
                answer.append(num)
        
        return answer