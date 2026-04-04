class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        sortedList=sorted(piles)
        maxNumber=sortedList[len(sortedList)-1]
        left=1
        right=maxNumber
        minAnswer=maxNumber
        while(left<=right):
            mid=(left+right)//2
            currentTotal=0
            for i in range(0,len(sortedList)):
                workHours=math.ceil(float(sortedList[i])/mid)
                currentTotal=currentTotal+workHours
            if(currentTotal<=h):
                minAnswer=mid
                right=mid-1
            else:
                left=mid+1
        return minAnswer
            



        