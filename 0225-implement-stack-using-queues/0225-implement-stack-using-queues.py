class MyStack:

    def __init__(self):
        self.q1 = []

    def push(self, x):
        self.q1.append(x)

    def pop(self):
        return self.q1.pop()
            

    def top(self):
        return self.q1[-1]
        
        
    def empty(self):
        if len(self.q1) == 0:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()