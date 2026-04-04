class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Hashset for each row
        for i in range(0,len(board)):
            setForRow=set()
            for j in range(0,len(board[i])):
                element=board[i][j]
                if(element!="," and element != "."):
                    if(element in setForRow):
                        return False
                    else:
                        if(element!="," and element!="."):
                            setForRow.add(element)
        #Hashset for each col
        for i in range(0,len(board)):
            setForCol=set()
            for j in range(0,len(board[i])):
                element=board[j][i]
                if(element!="," and element != "."):
                    if(element in setForCol):
                        return False
                    else:
                        setForCol.add(element)
        mapForGrid={}
        for i in range(0,3):
            for j in range(0,3):
                mapForGrid[(i,j)]=set()
        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                row=i//3
                col=j//3
                element=board[i][j]
                if(element!="," and element != "."):
                    if(board[i][j] in mapForGrid[(row,col)]):
                        print("here")
                        print(board[i][j])
                        return False
                    else:
                        if(element!="," and element!="."):
                            mapForGrid[(row,col)].add(board[i][j])
        return True
        