class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        count = {}
        for i in range(9):
            for j in range(9):
                number = board[i][j]
                if number == '.':
                    continue
                if count.get(number):
                    return False
                count[number] = 1
            count = {}
        
        for i in range(9):
            for j in range(9):
                number = board[j][i]
                if number == '.':
                    continue
                if count.get(number):
                    return False
                count[number] = 1
            count = {}


        i = 0
        j = 0
        while i < 9:
            while j < 9:
                for row in range(i,i+3):
                    for col in range(j,j+3):
                        number = board[row][col]
                        if number == '.':
                            continue
                        if count.get(number):
                            return False
                        count[number] = 1
                
                count = {}
                j += 3
            i+=3
        return True
                        