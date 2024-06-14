class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        sums = sum(arr[: k - 1])
        ans = 0
        
        for i in range(k - 1, len(arr)):
            sums += arr[i]
            if sums / k >= threshold:
                ans += 1
            sums -= arr[i - k + 1]
        
        
        return ans
        