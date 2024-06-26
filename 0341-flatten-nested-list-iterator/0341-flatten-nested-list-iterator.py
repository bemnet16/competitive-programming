# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.res = []
        self.idx = -1
        for item in nestedList:
            self.helper(item)
        
        
    def helper(self, ele):
        if ele.isInteger():
            self.res.append(ele.getInteger())
            return
        
        for item in ele.getList():
            self.helper(item)
        
    
    def next(self) -> int:
        self.idx += 1
        return self.res[self.idx]
        
    
    def hasNext(self) -> bool:
        return self.idx + 1 < len(self.res)
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())





























