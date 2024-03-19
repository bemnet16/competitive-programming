class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(left_half, right_half):
            
            left_half.append(float("inf"))
            right_half.append(float("inf"))
            merged_arr = []
            left_pointer = 0
            right_pointer = 0
            
            while left_pointer < len(left_half) and right_pointer < len(right_half):
                
                if left_half[left_pointer] < right_half[right_pointer]:
                    merged_arr.append(left_half[left_pointer])
                    left_pointer += 1
                
                else:
                    merged_arr.append(right_half[right_pointer])
                    right_pointer += 1
            
            # merged_arr.extend(left_half[left_pointer:])
            # merged_arr.extend(right_half[right_pointer:])
            
            merged_arr.pop()
            return merged_arr
        
        
        def mergeSort(left, right, arr):
            
            if left == right:
                return [arr[left]]
            
            mid = left + (right - left) // 2
            
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid + 1, right, arr)
            
            return merge(left_half, right_half)
        
        
        
        return mergeSort(0, len(nums) - 1, nums)
        