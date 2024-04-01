from collections import Counter
import math

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        counter = Counter(deck)
        minGroup = math.gcd(*list(counter.values()))
        
        return minGroup > 1

        