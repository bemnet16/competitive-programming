class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        right_greatest = -1
        
        for i in range((len(arr) - 1), -1, -1):
            
            tmp = arr[i]
            arr[i] = right_greatest
            right_greatest = max(right_greatest, tmp)
        
        
        
        return arr