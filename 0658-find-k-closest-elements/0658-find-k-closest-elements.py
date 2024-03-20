class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        temp = []
        
        for i in arr:
            temp.append(abs(i - x))
        
        l = 0
        
        for i in range(k, len(arr)):
            
            if temp[i] < temp[l]:
                while i - l + 1 > k:
                    l += 1
            
        
        return arr[l: l + k]
            
        
        