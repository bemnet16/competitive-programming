class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited_rooms = [0 for _ in range(len(rooms))]
        
        def dfs(room):
            
            visited_rooms[room] = 1
            
            for neighbour in rooms[room]:
                if not visited_rooms[neighbour]:
                    dfs(neighbour)
            
            
        dfs(0)
        return not visited_rooms.count(0)
        
        
        