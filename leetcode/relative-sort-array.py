class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        d = dict()
        re = []
        
        for n2 in arr2:
            d[n2] = 0
        
        for n1 in arr1:
            if n1 in d:
                d[n1] += 1
            else:
                re.append(n1)
        
        re.sort(reverse=True)
        
        idx = 0
        for n2 in arr2:
            for i in range(d[n2]):
                arr1[idx] = n2
                idx += 1
                
        for i,v in enumerate(re):
            arr1[-i - 1] = v
            
        return arr1
        