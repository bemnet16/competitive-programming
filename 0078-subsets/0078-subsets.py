class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        answer = []
        
        def backtrack(index, subset):
            
            if index >= len(nums):
                answer.append(subset.copy())
                return
            
            
            subset.append(nums[index])
            backtrack(index + 1, subset)
            subset.pop()
        
            backtrack(index + 1, subset)
        
        backtrack(0, [])
        return answer
        