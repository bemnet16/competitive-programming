class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        temp = []
        tot = len(nums1) + len(nums2)
        med = tot // 2
        print(med)
        
        if tot % 2 == 0:
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
            return (temp[-2] + temp[-1]) / 2.0
        else:
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
            return temp[-1]