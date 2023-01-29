class Solution:
    def solveSudoku(self, board):
    
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] !=".":
                    num = int(board[r][c])
                    row[r].add(num)
                    col[c].add(num)
                    box_id = r//3 * 3 + c//3
                    box[box_id].add(num)
        
        def backTrack(r,c):
            nonlocal solved
            if r==9:
                solved=True
                return
            new_r = r + (c+1) // 9
            new_c = (c+1) % 9

            if board[r][c]!=".":
                backTrack(new_r,new_c)
            else:
                for num in range(1,10):
                    box_id = r//3 *3 + c//3
                    if num not in row[r] and num not in col[c] and num not in box[box_id]:
                        row[r].add(num)
                        col[c].add(num)
                        box[box_id].add(num)
                        board[r][c] = str(num)

                        backTrack(new_r,new_c)

                        if not solved:
                            row[r].remove(num)
                            col[c].remove(num)
                            box[box_id].remove(num)
                            board[r][c]="."
        solved = False
        backTrack(0,0)


            