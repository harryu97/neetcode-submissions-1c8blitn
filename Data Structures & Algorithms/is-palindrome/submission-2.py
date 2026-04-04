class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        lowerCase=s.lower()
        print(lowerCase)
        while(left<=right):
            leftChar=lowerCase[left]
            rightChar=lowerCase[right]
            if(leftChar==rightChar):
                left+=1
                right-=1
                continue;
            if(leftChar.isdigit() is not True and leftChar.isalpha() is not True):
                print(leftChar)
                left+=1
            elif(rightChar.isdigit() is not True and rightChar.isalpha() is not True):
                print(rightChar)
                right-=1
            else:
                return False
        return True
                
        