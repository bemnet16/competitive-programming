class Solution(object):
    def heightChecker(self, heights):
        expected = heights[:]
        expected.sort()
        res = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                res += 1
        
        return res