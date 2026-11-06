class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = defaultdict(set)
        colMap = defaultdict(set)
        squareMap = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue

                if (board[row][col] in rowMap[row]) or \
                (board[row][col] in colMap[col]) or \
                (board[row][col] in squareMap[(row//3, col//3)]):
                    return False

                rowMap[row].add(board[row][col])
                colMap[col].add(board[row][col])
                squareMap[(row//3, col//3)].add(board[row][col])
        
        return True



        