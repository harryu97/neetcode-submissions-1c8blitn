class Solution:

    def encode(self, strs: List[str]) -> str:
        #Adding number and pound after each letter
        if(len(strs) == 0):
            return ""

        answer=[]
        p="#"
        for s in strs:
            p="#"
            lenOfString=str(len(s))
            lenOfString=lenOfString+p
            lenOfString=lenOfString+s
            answer.append(lenOfString)
        answerIntoString="".join(answer)
        print(f"This is input encoded {answerIntoString}")
        return answerIntoString

        

    def decode(self, s: str) -> List[str]:
        #With the encoded string
        #We alrady know it takes the length of letters and pound first
        if(len(s)==0):
            return []
        answer=[]
        i=0
        while i<len(s):
            j=i
            number=0
            while(s[j]!="#"):
                j+=1
            number=int(s[i:j])
            answer.append(s[j+1:j+1+number])
            i=j+1+number

        print(answer)
        return answer
