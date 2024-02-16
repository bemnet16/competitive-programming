class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.left = 0
        self.right = 0
        

    def consec(self, num: int) -> bool:
        if self.value == num:
            self.right += 1
        
        else:
            self.left = self.right
            
        
            
        if self.right - self.left < self.k:
            return False
        else:
            return True
        
        
        
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)