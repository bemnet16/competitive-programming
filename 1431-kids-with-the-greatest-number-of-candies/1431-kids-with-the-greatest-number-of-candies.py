class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        ans = [False] * len(candies)
        mx_candie = max(candies)
        
        for i, candie in enumerate(candies):
            if candie + extraCandies >= mx_candie:
                ans[i] = True
        
        
        return ans