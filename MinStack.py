class MinStack:
  def __init__(self):
    self.tem_li = []

  def push(self, x: int) -> None:
    mi = x if not self.tem_li else min(self.tem_li[-1][1], x)
    self.tem_li.append([x, mi])

  def pop(self) -> None:
    self.tem_li.pop()

  def top(self) -> int:
    return self.tem_li[-1][0]

  def getMin(self) -> int:
    return self.tem_li[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
