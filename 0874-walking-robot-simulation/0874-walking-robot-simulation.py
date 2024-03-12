class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        obs = defaultdict(set)
        
        for x, y in obstacles:
            obs[x].add(y)
        
        
        direction = ["N", "E", "S", "W"]
        cur_dir = 0
        coordinate = [0, 0]
        max_distance = 0
        
        for command in commands:
            
            if command == -1:
                cur_dir = (cur_dir + 1) % 4
            
            elif command == -2:
                cur_dir = (cur_dir - 1) % 4
            
            else:
                
                if cur_dir == 0:
                    for i in range(command):
                        if coordinate[1] + 1 in obs[coordinate[0]]:
                            break
                        
                        coordinate[1] += 1
                        
                elif cur_dir == 1:
                    for i in range(command):
                        if coordinate[1] in obs[coordinate[0] + 1]:
                            break
                        
                        coordinate[0] += 1
                        
                elif cur_dir == 2:
                    for i in range(command):
                        if coordinate[1] - 1 in obs[coordinate[0]]:
                            break
                        
                        coordinate[1] -= 1
                        
                elif cur_dir == 3:
                    for i in range(command):
                        if coordinate[1] in obs[coordinate[0] - 1]:
                            break
                        
                        coordinate[0] -= 1
                
                max_distance = max(max_distance, (coordinate[0] ** 2) + (coordinate[1] ** 2))
                        
                        
        return max_distance
    
    
    
    
    
    
    
    
    