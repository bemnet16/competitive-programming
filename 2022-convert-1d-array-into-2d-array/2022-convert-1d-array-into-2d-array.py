class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        if (m * n) != len(original):
            return []
        
        return [list(original[(i * n): (i * n + n)]) for i in range(m)]