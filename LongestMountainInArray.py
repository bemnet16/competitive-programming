class Solution(object):
    def longestMountain(self,arr):
        res=0
        for i,val in enumerate(arr):
            t=0
            l_v,r_v=val,val
            l,r=i-1,i+1
            lg=len(arr)
            if not((l>=0 and r<lg)and(arr[l]<l_v and arr[r]<r_v)):
                    continue
            while True:
                if (l>=0 and r<lg)and(arr[l]<l_v and arr[r]<r_v):
                    t+=2
                    l_v,r_v=arr[l],arr[r]
                    l-=1
                    r+=1
                elif l>=0 and arr[l]<l_v:
                    t+=1
                    l_v=arr[l]
                    l-=1
                elif r<lg and arr[r]<r_v:
                    t+=1
                    r_v=arr[r]
                    r+=1
                else:
                    break
            if t>=res:
                res=t+1
        if res>=3:
            return res
        return 0
