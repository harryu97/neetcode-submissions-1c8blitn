class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        if(len(nums)==0):
            return []
        #Make an array that contains the product 
        flagForOneZero=False
        flagForTwoZero=False
        totalProduct=1
        for i in nums:
            multiplier=0
            if(i==0):
                if(flagForTwoZero is False and flagForOneZero is False):
                    flagForOneZero=True
                    
                elif(flagForTwoZero is False and flagForOneZero is True):
                    flagForTwoZero=True
                multiplier=1
            else:
                multiplier=i
            totalProduct=totalProduct*multiplier
        
        answer=[]
        if(flagForTwoZero is True):
            return [0]*len(nums)
        for i in nums:
            if(flagForOneZero is True):
                if(i==0):
                    answer.append(totalProduct)        
                else:
                    answer.append(0)
            else:
                answer.append(totalProduct//i)
        print(answer)
        return answer

