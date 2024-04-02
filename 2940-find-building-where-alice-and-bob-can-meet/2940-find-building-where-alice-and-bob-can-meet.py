class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        
        stk = []
        for i,  height in enumerate(heights):
            
            while stk and heights[stk[-1]] < height:
                heights[stk[-1]] = (heights[stk[-1]], i)
                stk.pop()
            
            stk.append(i)
        
        while stk:
            heights[stk[-1]] = (heights[stk[-1]], -1)
            stk.pop()
        
        
        answer = []
        
        for a, b in queries:
            
            a, b = min(a, b),  max(a, b)
            
            if a == b:
                answer.append(a)
            
            elif a < b and heights[a][0] < heights[b][0]:
                answer.append(b)
            
            elif b < a and heights[b][0] < heights[a][0]:
                answer.append(a)
            
            else:
                if heights[a][1] == -1 or heights[b][1] == -1:
                    answer.append(-1)
                    
                elif heights[a][0] <= heights[b][0]:
                    answer.append(heights[b][1])
                
                else:
                    mx = heights[b]
                    while heights[a][0] >= heights[mx[1]][0]:
                        if heights[mx[1]][1] == -1:
                            mx = (-1, -1)
                            break
                            
                        mx = heights[mx[1]]
                        
                    answer.append(mx[1])
                    
                
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
#                 mx = max(heights[alice], heights[bob])
                
#                 low = 0
#                 high = len(heights) - 1
                
#                 while low <= high:
                    
#                     mid = low + (high - low) // 2
                    
#                     height, idx = sortedHeights[mid]

#                     if height <= mx:
#                         low = mid + 1
                    
#                     else:
#                         high = mid - 1
                
#                 if low < len(heights):
#                     print(low)
#                     answer[i] = sortedHeights[low][1]
        
#         return answer
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
            
            
            
        
        
        