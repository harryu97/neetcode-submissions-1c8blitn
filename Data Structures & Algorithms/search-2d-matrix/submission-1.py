class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Each row is ascending order
        #the last number in a row is smaller than the one in next row;

        #Find which row first with bst and then execute another bst 

        lR=0
        rR=len(matrix)-1
        while(lR<=rR):
            mid=(lR+rR)//2
            l=0
            r=len(matrix[mid])-1
            while(l<=r):
                midPoint=(l+r)//2
                if(target==matrix[mid][midPoint]):
                    return True
                if(target>matrix[mid][midPoint]):
                    l=midPoint+1
                else:
                    r=midPoint-1
            if(target>matrix[mid][0]):
                lR=mid+1
            else:
                rR=mid-1
        return False