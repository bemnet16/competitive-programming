class NumMatrix(object):

    def __init__(self, matrix):
        self.p_mat = [[0] * (len(matrix[0]) + 1) for i in range(len(matrix) + 1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.p_mat[i + 1][j + 1] = self.p_mat[i][j + 1] + self.p_mat[i + 1][j] + matrix[i][j] - self.p_mat[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        ## p_mat add 1 col and 1 row on matrix
        row1, col1 = row1 + 1, col1 + 1
        row2, col2 = row2 + 1, col2 + 1
        
        return self.p_mat[row2][col2] - self.p_mat[row1 - 1][col2] - self.p_mat[row2][col1 - 1] + self.p_mat[row1 - 1][col1 - 1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)