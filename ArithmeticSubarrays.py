class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for i in range(len(l)):
            lst_to_check = nums[l[i]:r[i] + 1]
            lst_to_check = sorted(lst_to_check)
            len_lst = len(lst_to_check)
            sum_t = ((lst_to_check[0] + lst_to_check[-1]) * len_lst)/ 2 
            if sum_t == sum(lst_to_check):
                d = lst_to_check[-1] - lst_to_check[-2]
                for num in lst_to_check:
                    checked = True
                    for j in range(lst_to_check.index(num) + 1, len(lst_to_check)):
                        if lst_to_check[j] - lst_to_check[j -1] != d:
                            res.append(False)
                            checked = False
                            break
                    if not checked:
                        break
                if not checked:
                    continue
                res.append(True)
            else:
                res.append(False)
        return res
