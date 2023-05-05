class Solution(object):
    def lastStoneWeight(self, stones):
        if len(stones)==1:
                return stones[0]
        stones.sort()
        while stones:
            y=stones.pop()
            x=stones.pop()
            if x!=y:
                stones.append(y-x)
                stones.sort()
            if len(stones)==1:
                return stones[0]
        return 0
