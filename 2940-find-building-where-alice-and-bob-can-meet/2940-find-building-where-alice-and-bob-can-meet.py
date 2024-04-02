class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        
        ### Monotonic stack approach ###
        
        # update heights to hold there index with there height value.
        # add '-1' for heights that has no larger height on the right.

        stack = []

        for i,  height in enumerate(heights):
            
            while stack and heights[stack[-1]] < height:
                heights[stack[-1]] = (heights[stack[-1]], i)
                stack.pop()
            stack.append(i)
        
        while stack:
            heights[stack[-1]] = (heights[stack[-1]], -1)
            stack.pop()
        

        
        answer = []
        
        for alice, bob in queries:
            
            alice, bob = min(alice, bob), max(alice, bob)
            
            if alice == bob:
                answer.append(alice)
            
            elif heights[alice][0] < heights[bob][0]:
                answer.append(bob)
            
            elif heights[alice][0] == heights[bob][0]:
                answer.append(heights[bob][1])

            elif heights[alice][1] == -1 or heights[bob][1] == -1:
                answer.append(-1)

            else:
                maxHeight = heights[bob]
                while heights[alice][0] >= heights[maxHeight[1]][0]:
                    if heights[maxHeight[1]][1] == -1:
                        maxHeight = (-1, -1)
                        break
                        
                    maxHeight = heights[maxHeight[1]]
                    
                answer.append(maxHeight[1])
                
                
        return answer
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         sortedHeights = []
        
#         for i, height in enumerate(heights):
#             sortedHeights.append((height, i))
        
        
#         sortedHeights.sort(key=lambda x:x[0])
        
        
#         answer = [-1 for _ in range(len(queries))]
        
        
#         for i, query in enumerate(queries):
            
#             alice, bob = min(query), max(query)
            
#             if alice == bob:
#                 answer[i] = alice
            
#             elif heights[bob] >= heights[alice]:
#                 answer[i] = bob
            
#             else:
#                 maxHeight = max(heights[alice], heights[bob])
                
#                 low = 0
#                 high = len(heights) - 1
                
#                 while low <= high:
                    
#                     mid = low + (high - low) // 2
                    
#                     height, idx = sortedHeights[mid]

#                     if height <= maxHeight:
#                         low = mid + 1
                    
#                     else:
#                         high = mid - 1
                
#                 if low < len(heights):
#                     print(low)
#                     answer[i] = sortedHeights[low][1]
        
#         return answer
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
            
            
            
        
        
        