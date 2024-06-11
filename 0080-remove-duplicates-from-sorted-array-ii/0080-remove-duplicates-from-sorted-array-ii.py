class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        cur = nums[0]
        s = [cur]
        idx = 1
        
        for i in range(1, len(nums)):
            
            if cur == nums[i] and len(s) < 2:
                nums[idx], nums[i] = nums[i], nums[idx]
                s.append(cur)
                idx += 1
            
            elif cur != nums[i]:
                nums[idx], nums[i] = nums[i], nums[idx]
                cur = nums[idx]
                s = [cur]
                idx += 1
        
        return idx
        
        