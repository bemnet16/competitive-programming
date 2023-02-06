class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2:
            return []
        chgArr=[]
        
        temp=Counter(changed)
        changed.sort()
        for number in changed:
            if number==0 and temp[number]>=2:
                chgArr.append(number)
                temp[number]-=2
            if number>0  and temp[number] and temp[2*number]:
                chgArr.append(number)
                temp[number]-=1
                temp[2*number]-=1
        if len(chgArr)==len(changed)//2:
            return chgArr
        return []

    
    ### Those also work with some expetion values
    
   # def findOriginalArray(changed):
        
#         lg = len(changed)
#         if lg <= 1 and lg % 2 != 0:
#             return []
#         elif (changed[0] * 2) == changed[int(lg/2)]:
#             for i in range(int(lg/2)):
#                 if (changed[i] * 2) != changed[i + int(lg/2)]:
#                     return []
#         elif (changed[0]) == changed[int(lg/2)] * 2:
#             for i in range(int(lg/2)):
#                 if changed[i] != changed[i + int(lg/2)] * 2:
#                     return []
#             changed = changed[::-1]
#         else:
#             return []
            
#         return changed[:int(lg/2)]
        

  
  
# class Solution(object):
#     def findOriginalArray(self, changed):

#         if len(changed) <= 1 or len(changed) % 2 != 0:
#             return []

#         lg = int(len(changed)/2)
#         left = changed[:lg]
#         right = changed[lg:]
#         left.sort(),right.sort()
        
        
#         if left[0] * 2 == right[0] or left[-1] * 2 == right[-1]:
#             for i in range(lg):
#                 if left[i] * 2 != right[i]:
#                     return []
#         elif left[0] == right[0] * 2 and left[-1] == right[-1] * 2:
#             for i in range(lg):
#                 if left[i] != right[i] * 2:
#                     return []
#             left, right = right, left
#         elif  left[0] * 2 != right[0] or left[-1] * 2 != right[-1] and len(left) >= 4:
#             return []
       

#         return left
