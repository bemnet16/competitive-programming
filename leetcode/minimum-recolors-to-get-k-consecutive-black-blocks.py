class Solution(object):
    def minimumRecolors(self, blocks, k):
        
#         i=res=0
#         while i<len(blocks):
#             temp=j=0
#             while j<k:
#                 if (j+i)<len(blocks):
#                     if blocks[j+i]=='B':
#                         temp+=1
#                 j+=1
#             if temp>res:
#                 res=temp
#             i+=1
#         return k-res
    
    #count no of W from index 0 = i to k
    #then proceed by 1 in each iterative
    #if blocks i is w count reduce by one 
    # if k+1 is W count reduce by 1 
    # if B no change
    #return count
        
        res=float("inf")
        min_count=0
        for i in range(k):
            if blocks[i]=="W":
                min_count+=1
        res=min(res,min_count)
        for i in range(k,len(blocks)):
            if blocks[i-k]=="W":
                min_count-=1
            if blocks[i]=="W":
                min_count+=1
            res=min(res,min_count)
        return res