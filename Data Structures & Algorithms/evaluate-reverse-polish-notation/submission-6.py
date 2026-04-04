from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=deque();
        if(len(tokens)==1):
            return int(tokens[-1])
        for i in tokens:
            if(i=="+" or i=="-" or i=="*" or i=="/"):
                curr=int(stack.pop())
                numb=int(stack.pop())
                result=0
                if(i=="+"):
                    result=numb+curr
                elif(i=="-"):
                    result=numb-curr
                elif(i=="*"):
                    result=numb*curr
                else:
                    result=int(numb/curr)
                stack.append(result)
                print(stack)
            else:
                stack.append(i)
        return stack[-1]
