class Node:
    def __init__(self,val=""):
        self.prev = None
        self.val = val
        self.next = None
        
class BrowserHistory:

    def __init__(self, homepage):
        self.cur_history = Node(homepage)

    def visit(self, url):
        
        new_history = Node(url)
        new_history.prev = self.cur_history
        
        self.cur_history.next = new_history
        self.cur_history = self.cur_history.next

    def back(self, steps):
        
        for _ in range(steps):
            if self.cur_history.prev:
                self.cur_history = self.cur_history.prev
            else:
                break

        return self.cur_history.val

    def forward(self, steps):
        
        for _ in range(steps):
            if self.cur_history.next:
                self.cur_history = self.cur_history.next
            else:
                break
        
        return self.cur_history.val

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)