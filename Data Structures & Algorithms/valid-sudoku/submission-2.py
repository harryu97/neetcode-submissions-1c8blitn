from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #First u check the row with hashset
        #Second u check the col with hashset
        #Third u make hashmap

        for i in range(0,len(board)):
            currentSet=set()
            for j in range(0,len(board[i])):
                currentElement=board[i][j]
                if(currentElement in currentSet):
                    return False
                else:
                    if(currentElement !="." and currentElement!=","):
                        currentSet.add(currentElement)
        
        for i in range(0,len(board)):
            currentSet=set()
            for j in range (0,len(board[i])):
                currentElement=board[j][i]
                if(currentElement in currentSet):
                    return False
                else:
                    if(currentElement !="." and currentElement!=","):
                        currentSet.add(currentElement)
        
        gridDict=defaultdict(set)
        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                gridX=i//3
                gridY=j//3
                currentelement=board[i][j]
                if(currentelement in gridDict[(gridX,gridY)]):
                    return False
                else:
                    if(currentelement !="." and currentelement!=","):
                        gridDict[(gridX,gridY)].add(currentelement)

        return True
                