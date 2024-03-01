class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        
        count = 0
        
        for i in range(len(nums) - 2):
            k = i + 2
            if nums[i] == 0:
                continue 
            for j in range((i + 1), len(nums)):
                while k < len(nums) and nums[i] + nums[j] > nums[k]:
                    k += 1
                
                count += (k - j - 1)
        
        
        return count
        
        
        ######## Brute Force approach TLE ########
        
#         def isValidTriangle(side1, side2, side3):
#             if (side1 + side2) > side3 and (side2 + side3) > side1 and (side1 + side3) > side2:
#                 return True
            
#             return False
        
        
#         num_triangles = 0
        
        
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 for k in range((j + 1), len(nums)):
                    
#                     if isValidTriangle(nums[i], nums[j], nums[k]):
#                         num_triangles += 1
        
        
        
#         return num_triangles
        
        
        ######### TLE for Binary Tree search approach ###########
        
#         self.triangles = 0
        
#         def isValid(arr):
            
#             side1, side2, side3= arr
            
#             if (side1 + side2) > side3 and (side2 + side3) > side1 and (side1 + side3) > side2:
#                 return True
            
#             return False
        
        
#         def dfs(index, sides):
            
#             if len(sides) == 3:
#                 if isValid(sides):
#                     self.triangles += 1
#                 return
            
#             if index >= len(nums):
#                 return
            
#             sides.append(nums[index])
#             dfs(index + 1, sides)
#             sides.pop()
            
            
#             dfs(index + 1, sides)
        
        
        
#         dfs(0, [])
#         return self.triangles
            
            
                
        