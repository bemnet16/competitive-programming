class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        
        answer = 0
        current_value = nums[-1]
        
        for i in range(len(nums) - 2, -1, -1):
            
            if nums[i] > current_value:
                space = ceil(nums[i] / current_value)  # divde optimaly within the space
                answer += (space - 1)      # perfomed space - 1 operations
                current_value = nums[i] // space  # the minimum value after the operation
                
            else:
                current_value = nums[i]
        
        return answer