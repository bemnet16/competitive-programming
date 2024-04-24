class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        unused_rooms = [i for i in range(n)]
        used_rooms = []
        meeting_count = [0] * n
        heapify(unused_rooms)
        
        for start, end in sorted(meetings):
            
            while used_rooms and used_rooms[0][0] <= start:
                _, room = heappop(used_rooms)
                heappush(unused_rooms, room)
            
            if unused_rooms:
                room = heappop(unused_rooms)
                heappush(used_rooms, (end, room))
                meeting_count[room] += 1
            else:
                e, room = heappop(used_rooms)
                heappush(used_rooms, ((e + (end - start)), room))
                meeting_count[room] += 1
        
        
        return meeting_count.index(max(meeting_count))
        