class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left=0
        right=len(heights)-1
        answer=0
        while(left<right):
            leftHeight=heights[left]
            rightHeight=heights[right]
            current=(right-left)*min(leftHeight,rightHeight)
            answer=max(answer,current)
            if(leftHeight<rightHeight):
                left+=1
            else:
                right-=1
        return answer
            