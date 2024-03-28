class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        
        if not self.store[key]:
            return ""
        
        low = 0
        high = len(self.store[key]) - 1
        
        while low <= high:
            
            mid = low + (high - low) // 2
            
            value, saved_timestamp = self.store[key][mid]
            
            if saved_timestamp > timestamp:
                high = mid - 1
            
            else:
                low = mid + 1
        
        
        return self.store[key][high][0] if timestamp >= self.store[key][high][1] else ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)