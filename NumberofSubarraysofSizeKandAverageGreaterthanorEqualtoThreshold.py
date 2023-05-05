class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        tot,num=0,0
        for i in range(len(arr)):
            if i>=k-1:
                tot+=arr[i]
                if tot/k >= threshold:
                    num+=1
                tot-=arr[i-k+1]
            else:
                tot+=arr[i]
        return num
