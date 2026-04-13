class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqS1={}
        if(len(s1)>len(s2)):
            return False
        for c in s1:
            count=1+freqS1.get(c,0)
            freqS1[c]=count
        left=0
        right=len(s1)
        while(right<len(s2)+1):
            currentFreq={}
            for i in range(left,right):
                count=1+currentFreq.get(s2[i],0)
                currentFreq[s2[i]]=count
            print(f"Current Freq {currentFreq}")
            if(currentFreq==freqS1):
                return True
            else:
                left+=1
                right+=1
        return False
                

