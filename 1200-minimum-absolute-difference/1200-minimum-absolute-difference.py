class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        res = []
        mi=float("inf")
        
        for i in range(1,len(arr)):
            if arr[i] - arr[i - 1] < mi:
                res = []
                mi = arr[i] - arr[i - 1]
                res.append([arr[i - 1], arr[i]])
            elif arr[i] - arr[i - 1] == mi:
                res.append([arr[i - 1], arr[i]])
            
        return res
                