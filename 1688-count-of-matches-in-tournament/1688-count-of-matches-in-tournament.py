class Solution(object):
    def numberOfMatches(self, n):
        matches = 0
        while n > 1:
            if n % 2 == 0:
                n //=2
                matches += n
            else:
                matches += (n - 1) // 2
                n = ((n - 1) // 2) + 1
        
        return matches