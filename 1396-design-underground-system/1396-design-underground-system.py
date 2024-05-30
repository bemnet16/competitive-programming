class UndergroundSystem:

    def __init__(self):
        self.checks = defaultdict(list)
        self.avaTimes = defaultdict(list)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checks[id].append((stationName, t))
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        station, time = self.checks[id].pop()
        self.avaTimes[(station + "-" + stationName)].append(t - time)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        _sum = sum(self.avaTimes[(startStation + "-" + endStation)])
        lg = len(self.avaTimes[(startStation + "-" + endStation)])
        return _sum / lg
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)