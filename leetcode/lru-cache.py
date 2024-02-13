from collections import OrderedDict
class LRUCache(object):

    def __init__(self, capacity):
        self.capacity=capacity
        self.cache=OrderedDict()

    def get(self, key):
        if key in self.cache:
            self.cache[key]=self.cache.pop(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache[key]=self.cache.pop(key)
        elif len(self.cache)==self.capacity:
            self.cache.popitem(last=False)
        self.cache[key]=value
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)