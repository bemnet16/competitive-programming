from sortedcontainers import SortedList
import bisect

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        
        
        sortedArray = SortedList()
        cost = 0
        
        for instruction in instructions:
            left_cost = sortedArray.bisect_left(instruction)
            right_cost = len(sortedArray) - sortedArray.bisect_right(instruction)
            cost += min(left_cost, right_cost)
            sortedArray.add(instruction)
        
        return cost % (10 ** 9 + 7)
        
        
        
