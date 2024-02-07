class NumMatrix(object):

    def __init__(self, matrix):
        self.prefix = [[0] * (len(matrix[0]) + 1) for i in range(len(matrix) + 1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.prefix [i + 1][j + 1] = self.prefix[i][j + 1] + self.prefix[i + 1][j] - self.prefix[i][j] + matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        row1 += 1
        row2 += 1
        col1 += 1
        col2 += 1
        return self.prefix[row2][col2] - self.prefix[row2][col1 - 1] - self.prefix[row1 - 1][col2] + self.prefix[row1 - 1][col1 - 1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)