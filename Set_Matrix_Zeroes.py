class Solution:
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])  # m is col and n is row
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0
        if first_row_has_zero:
            matrix[0] = [0] * n
