class Solution(object):
    def sortByBits(self, arr):
        
        for i,v in enumerate(arr):
            arr[i] = [bin(v).count('1'),v]
            
        arr.sort(key=lambda x:(x[0], x[1]))
        
        for i,v in enumerate(arr):
            arr[i] = arr[i][1]
            
        return arr