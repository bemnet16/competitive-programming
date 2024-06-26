class FreqStack:

    def __init__(self):
        self.ele = defaultdict(list)
        self.freq = defaultdict(int)
        self.mx = 0
        

    def push(self, val: int) -> None:
        self.freq[val] += 1
        f = self.freq[val]
        self.mx = max(self.mx, f)
        self.ele[f].append(val)
        
        
        

    def pop(self) -> int:
        top = self.ele[self.mx].pop()
        self.freq[top] -= 1
        if not self.ele[self.mx]:
            self.mx -= 1
        return top


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()