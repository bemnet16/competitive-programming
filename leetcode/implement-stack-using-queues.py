class MyStack(object):

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x):
        self.q1.append(x)

    def pop(self):
        for i in range(len(self.q1) - 1):
            self.q2.append(self.q1.pop(0))
        self.q1, self.q2 = self.q2,self.q1
        return self.q2.pop(0)
            

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