class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        ans = 0
        for i in range(len(mat)):
            ans += mat[i][i]
            ans += mat[i][len(mat) - 1 - i]
        
        rm = len(mat)
        if rm % 2 == 1:
            ans -= mat[rm // 2][rm // 2]
        
        return ans