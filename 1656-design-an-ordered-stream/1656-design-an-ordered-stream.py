class OrderedStream:

    def __init__(self, n: int):
        self.ss = []
        self.cur = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        if idKey != self.cur:
            heappush(self.ss, (idKey, value))
            return []
        
        stream = [value]
        self.cur += 1
        while self.ss and self.ss[0][0] == self.cur:
            stream.append(heappop(self.ss)[1])
            self.cur += 1
            
        return stream
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)