from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        result=deque()
        if(len(s)==1):
            return False
        for c in s:
            if(c=="[" or c=="(" or c=="{"):
                result.append(c)
            else:
                if(len(result)==0):
                    return False
                lastElement=result[-1]
                if(lastElement=="[" and c=="]"):
                    result.pop()
                elif(lastElement=="(" and c==")"):
                    result.pop()
                elif(lastElement=="{" and c=="}"):
                    result.pop()
                else:
                    result.append(c)
        if(len(result)>0):
            return False
        return True