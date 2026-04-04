from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]
        for index in range(0,len(temperatures)):
            temp=temperatures[index]
            while(stack and temp>stack[-1][0]):
                elem,elemIndex=stack.pop()
                res[elemIndex]=index-elemIndex
            stack.append([temp,index])
        return res