class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        
        if numOnes >= k:
            return k
        
        answer = numOnes
        k -= numOnes
        if numZeros >= k:
            return answer
        
        k -= numZeros
        answer -= k
        return answer
        