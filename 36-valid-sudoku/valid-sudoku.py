class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #initialize 2 other versions of the board
        board_columnwise = []
        board_3x3wise = []

       


        for i in range(9):
            board_columnwise.append([".",".",".",".",".",".",".",".","."])
            board_3x3wise.append([".",".",".",".",".",".",".",".","."])


        #create the column wise board
        for j in range(9):
            for k in range (9):
                board_columnwise[j][k] = board[k][j]

                
        #create the 3x3 wise board
        for x in range(0,7,3):
            for l in range(3):
                board_3x3wise[x][l] = board[x][l]
            for a in range(3,6):
                board_3x3wise[x+1][a-3] = board[x][a]
            for b in range(6,9):
                board_3x3wise[x+2][b-6] = board[x][b]
                
        for y in range(1,8,3):      
            for m in range(3,6):
                board_3x3wise[y][m] = board[y][m]
            for c in range(6,9):
                board_3x3wise[y+1][c-3] = board[y][c]
            for d in range(3):
                board_3x3wise[y-1][d+3] = board[y][d]
                
        for z in range(2,9,3): 
            for n in range(6,9):
                board_3x3wise[z][n] = board[z][n]
            for e in range(3):
                board_3x3wise[z-2][e+6] = board[z][e]
            for f in range(3,6):
                board_3x3wise[z-1][f+3] = board[z][f]

            

        #so now we have 3 versions of the board and all of them must pass the test of no repeats in each sub list
    
        for row in board:
            for num_space_row in range(row.count(".")):
                row.remove(".")
        for row_columnwise in board_columnwise:
            for num_space_rowcolumnwise in range(row_columnwise.count(".")):
                row_columnwise.remove(".")
        for row_3x3wise in board_3x3wise:
            for num_space_row3x3wise in range(row_3x3wise.count(".")):
                row_3x3wise.remove(".")


        
        return len(board[0]) == len(set(board[0])) and len(board_columnwise[0]) == len(set(board_columnwise[0])) and len(board_3x3wise[0]) == len(set(board_3x3wise[0])) and len(board[1]) == len(set(board[1])) and len(board_columnwise[1]) == len(set(board_columnwise[1])) and len(board_3x3wise[1]) == len(set(board_3x3wise[1])) and len(board[2]) == len(set(board[2])) and len(board_columnwise[2]) == len(set(board_columnwise[2])) and len(board_3x3wise[2]) == len(set(board_3x3wise[2])) and len(board[3]) == len(set(board[3])) and len(board_columnwise[3]) == len(set(board_columnwise[3])) and len(board_3x3wise[3]) == len(set(board_3x3wise[3])) and len(board[4]) == len(set(board[4])) and len(board_columnwise[4]) == len(set(board_columnwise[4])) and len(board_3x3wise[4]) == len(set(board_3x3wise[4])) and len(board[5]) == len(set(board[5])) and len(board_columnwise[5]) == len(set(board_columnwise[5])) and len(board_3x3wise[5]) == len(set(board_3x3wise[5])) and len(board[6]) == len(set(board[6])) and len(board_columnwise[6]) == len(set(board_columnwise[6])) and len(board_3x3wise[6]) == len(set(board_3x3wise[6])) and len(board[7]) == len(set(board[7])) and len(board_columnwise[7]) == len(set(board_columnwise[7])) and len(board_3x3wise[7]) == len(set(board_3x3wise[7])) and len(board[8]) == len(set(board[8])) and len(board_columnwise[8]) == len(set(board_columnwise[8])) and len(board_3x3wise[8]) == len(set(board_3x3wise[8]))
                
            