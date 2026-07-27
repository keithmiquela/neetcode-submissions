class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            for i in range(1,10):
                if row.count(str(i))>1:
                    return False
        for i in range(0,9):
            dictionary={}
            for j in range(0,9):
                if not dictionary.get(board[j][i]) or board[j][i]==".":
                    dictionary[board[j][i]]=1
                else:
                    return False
        for i in range (0,9):
            dictionary={}
            for j in range(0,9):
                if not dictionary.get(board[(int(i/3))*3+int(j/3)][(i%3)*3+j%3]) or board[(int(i/3))*3+int(j/3)][(i%3)*3+j%3]==".":
                    dictionary[board[(int(i/3))*3+int(j/3)][(i%3)*3+j%3]]=1
                else:
                    return False
        return True