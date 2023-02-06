class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        repo = []
        dict_temp = {}

        for i in nums2:
            while repo and repo[-1] < i:
                num = repo.pop()
                dict_temp[num] = i
            repo.append(i)

        for i in range(len(nums1)):
            if nums1[i] in dict_temp:
                nums1[i] = dict_temp[nums1[i]]
            else:
                nums1[i] = -1

        return nums1
