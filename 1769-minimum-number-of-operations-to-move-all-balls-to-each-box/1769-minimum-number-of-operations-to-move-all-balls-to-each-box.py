class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        ans = [0] * len(boxes)
        
        for i in range(len(boxes)):
            for j in range(len(boxes)):
                if boxes[j] == "1":
                    ans[i] += abs(i - j)
        
        
        return ans
        