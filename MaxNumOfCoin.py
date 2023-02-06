class Solution(object):
    def maxCoins(self, piles):
       
        piles.sort()
        coin = 0
        left = 0
        right = len(piles)-1
        while left < (right-1):
            index = len(piles)-1
            triplet = (piles[left],piles[right-1],piles[right]) 
            coin += piles[right-1]
            left += 1
            right -= 2
        return coin
