class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        distance = []
        
        for num in arr:
            distance.append(abs(num - x))
        
        start = 0
        
        for i in range(k, len(arr)):
            
            if distance[i] < distance[start]:
                while i - start + 1 > k:
                    start += 1
            
        
        return arr[start: start + k]
            
        
        