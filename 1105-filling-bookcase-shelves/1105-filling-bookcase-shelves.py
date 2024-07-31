class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        dp = [0]
        for i in range(len(books)):
            res = float('inf')
            widths = 0
            maxi = 0
            for j in range(i,-1,-1):
                widths += books[j][0]
                maxi = max(maxi,books[j][1])
                if widths > shelfWidth:break 
                res = min(res,dp[j]+maxi)
            dp.append(res)
        return dp[-1]