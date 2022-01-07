class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen=[]         # <---------------- stores every element in a structured format
        for i,r in enumerate(board):     # <---------- each row
            for j,c in enumerate(r):      # <----------- each column
                if c != '.':       # <--------- if the character is not a '.'
                    seen += [(i,c),(c,j),(i//3,j//3,c)]     # <-------- keep adding those structured elements in the list
        return len(seen)==len(set(seen))     # <------ if there is any duplicate elements stored in the list then its not in sudoku format