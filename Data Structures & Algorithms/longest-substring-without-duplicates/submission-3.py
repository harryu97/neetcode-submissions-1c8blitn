from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        currentList=deque()
        answer=0
        if(len(s)==1):
            return 1
        while(right<len(s)):
            #Check only there is one more after this loop
        

            currentChar=s[right] # 0th index
            
            if(currentChar in currentList):
                while(currentChar in currentList):
                    currentList.popleft()
            currentList.append(currentChar)
            right+=1

            print(f"Len{len(currentList)}")
            answer=max(answer,len(currentList))
        return answer