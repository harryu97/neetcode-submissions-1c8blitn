from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if(len(nums)==0):
            return []
        dict=defaultdict(int)
        for i in nums:
            dict[i]=dict[i]+1
        freq=[]
        for num,count in dict.items():
            freq.append([count,num])
        print(freq)
        freq.sort()
        answer=[]
        for i in range(0,k):
            answer.append(freq[len(freq)-1-i][1])
        print(answer)
        return answer
