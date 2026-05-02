class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r=max(piles)
        left=1
        answer=r 
        while(left<=r):
            mid=(r+left)//2
            total=0
            for i in piles:
                total+=math.ceil(i/mid)
            if(total<=h):
                answer=min(answer,mid)
                r=mid-1
            else:
                left=mid+1
        return answer