class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr=0
        left=0
        for i in range(0,len(prices)):
            if(i==0):
                continue;
            if(i>0):
                possibleTotal=prices[i]-prices[i-1]
                currentTotal=prices[i]-prices[left]
                print(f"prices[i]={prices[i]} ")
                print(f"current Left={left}")
                print(f"current={curr}")
                print(f"possibleTotal={possibleTotal}")
                if(possibleTotal>currentTotal and possibleTotal>0):
                    left=i-1
                    curr=max(curr,possibleTotal)
                else:
                    curr=max(curr,currentTotal)
        return curr
                

        