class MinStack:

    def __init__(self):
        self.mlist=[]
        self.minimumList=[]

        

    def push(self, val: int) -> None:
        self.mlist.append(val)
        if(len(self.minimumList)!=0):
            lastElement=self.minimumList[-1]
            if(val>lastElement):
                val=lastElement
        self.minimumList.append(val)
    def pop(self) -> None:
        self.mlist.pop()
        self.minimumList.pop()
    def top(self) -> int:
        return self.mlist[-1]
        
    def getMin(self) -> int:
        return self.minimumList[-1]        

        
