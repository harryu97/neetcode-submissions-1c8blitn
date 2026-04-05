class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        answer=[]
        for i in range(0,len(nums)):
           
            pivot=nums[i]
            left=i+1
            right=len(nums)-1
            if(pivot>0):
                break;
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while(left<right):
                
                leftNum=nums[left]
                rightNum=nums[right]
                total=pivot+leftNum+rightNum
                if(total<0):
                    left+=1
                elif(total>0):
                    right-=1
                else:
                    answer.append([pivot,leftNum,rightNum])
                    left+=1
                    right-=1
                    while(left<right and nums[left]==nums[left-1]):
                        left+=1
        return answer