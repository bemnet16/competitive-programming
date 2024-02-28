class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            
            cur_sum = numbers[left] + numbers[right]
            
            if cur_sum < target:
                left += 1
            elif cur_sum > target:
                right -= 1
            else:
                return [(left + 1), (right + 1)]
        
        
#         left = 0
#         right = 1
        
#         while right < len(numbers):
            
#             cur_sum = numbers[left] + numbers[right]
#             if cur_sum == target:
#                 return [(left + 1), (right + 1)]
            
#             elif cur_sum > target:
#                 left += 1
#                 right = left + 1
            
#             elif right == len(numbers) - 1:
#                 left += 1
#                 right = left + 1
                
#             else:   
#                 right += 1
        
        
        
#         left, right = 0, 1
        
#         while right < len(numbers):
            
#             s_temp = numbers[left] + numbers[right]
            
#             if s_temp < target and right == len(numbers) - 1:
#                 left += 1
#                 right = left + 1
            
#             elif s_temp < target:
#                 right += 1
            
#             elif s_temp > target:
#                 left += 1
            
#             else:
#                 return [(left + 1), (right + 1)]
        