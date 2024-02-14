class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # at here we are sure to reach the last index, since it is the last indext itself.
        good_position = len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            
            # update the good pos. since we can reach the last index from the good pos. near to the current index
            if nums[i] >= good_position - i:
                good_position = i
        
        # if good pos. comes to the start we are sure that we can reach at last index start from first index
        if good_position == 0:
            return True
        return False