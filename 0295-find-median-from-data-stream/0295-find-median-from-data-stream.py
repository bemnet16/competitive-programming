class MedianFinder(object):

    def __init__(self):
        
        self.minHeap = []
        self.maxHeap = []
        

    def addNum(self, num):
        
        heappush(self.maxHeap, -num)
        
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        
        elif self.minHeap and -self.maxHeap[0] > self.minHeap[0]:
            heappush(self.minHeap, -heappop(self.maxHeap))
            heappush(self.maxHeap, -heappop(self.minHeap))
            
            
            
    def findMedian(self):
        
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        
        return (-self.maxHeap[0] + self.minHeap[0]) / 2.0


    
    
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()