def findOriginalArray(changed):
        
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
        

  
  
  class Solution(object):
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

