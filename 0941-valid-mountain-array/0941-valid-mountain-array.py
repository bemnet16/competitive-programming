class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        max_value = max(arr)
        max_index = arr.index(max_value)
        
        if max_index == 0 or max_index == (len(arr) - 1):
            return False
        
        for i in range(max_index):
            if arr[i] >= max_value or arr[i] >= arr[i + 1]:
                return False
        
        for i in range((max_index + 1), len(arr)):
            if arr[i] >= max_value or arr[i - 1] <= arr[i]:
                return False
        
        return True
        
