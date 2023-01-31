class Solution:
    def solveNQueens(self, n: int):
        def is_not_under_attack(row,col):
            return not (rows[col] or hills[row-col] or dales[row+col])
        
        def place_Queen(row,col):
            rows[col] = 1
            hills [row-col] = 1
            dales [row+col] = 1

        def remove_Queen(row,col):
            rows[col] = 0
            hills[row-col] = 0
            dales[row+col] = 0

        def backtrack(row=0, partial_result=[]):
            if row == n:
                result.append(partial_result)
            for col in range(n):
                if is_not_under_attack(row,col):
                    place_Queen(row,col)
                    backtrack(row+1, partial_result+[col])
                    remove_Queen(row,col)
        result = []
        rows = [0] * n
        hills = [0] * (2 * n - 1) 
        dales = [0] * (2 * n - 1)  
        backtrack()

        return [['.' * col + 'Q' + '.' * (n - col - 1) for col in solution] for solution in result]
