from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dict=defaultdict(int)
        for i in nums:
            dict[i]=dict[i]+1
        freq=[]
        for num,cnt in dict.items():
            freq.append([cnt,num])
        freq.sort()

        res=[]
        while(len(res)<k):
            res.append(freq.pop()[1])
        print(freq)
        #The size of input value is already done 
        return res