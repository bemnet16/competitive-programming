class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        temp = []
        tot = len(nums1) + len(nums2)
        med = tot // 2
        print(med)
        
        i,j = 0,0
        for k in range(med + 1):
            if i >= len(nums1):
                temp.append(nums2[j])
                j += 1
            elif j >= len(nums2):
                temp.append(nums1[i])
                i += 1
            elif nums1[i] < nums2[j]:
                temp.append(nums1[i])
                i += 1
            else:
                temp.append(nums2[j])
                j += 1
        
        if tot % 2 == 0:
            return (temp[-2] + temp[-1]) / 2.0
        else:
            return temp[-1]
        
#         class Solution(object):
#     def findMedianSortedArrays(self, nums1, nums2):
#         tot = len(nums1) + len(nums2)
#         med = tot // 2
        
#         i,j = 0,0
#         for k in range(med + 1):
#             if i >= len(nums1): j += 1
#             elif j >= len(nums2): i += 1
#             elif nums1[i] < nums2[j]: i += 1
#             else: j += 1
                
#         if tot % 2 == 0:
#             if (i - 1) < 0:
#                 return (nums2[j - 1] + nums2[j - 2] ) / 2.0
#             elif (j - 1) < 0:
#                 return (nums1[i - 1] + nums1[i - 2] ) / 2.0
                
#             return (nums1[i - 1] + nums2[j - 1] ) / 2.0
        
#         else:
#             if (i - 1) < 0:
#                 return nums2[j - 1]
#             elif (j - 1) < 0:
#                 return nums1[i - 1]
            
#             return max(nums1[i - 1] , nums2[j - 1])
        
     