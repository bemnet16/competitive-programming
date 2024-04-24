class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        meetings.sort(key=lambda x:x[0])
        
        mostMeet = 0
        roomAvailability = [0] * n
        countMeeting = [0] * n
        
        for start, end in meetings:
            
            minAvaIdx = 0
            hasUnusedRoom = False
            
            for i, availability in enumerate(roomAvailability):
                
                if availability < roomAvailability[minAvaIdx]:
                    minAvaIdx = i
                
                if availability <= start:
                    hasUnusedRoom = True
                    roomAvailability[i] = end
                    countMeeting[i] += 1
                    mostMeet = max(mostMeet, countMeeting[i])
                    break
            
            if not hasUnusedRoom:
                roomAvailability[minAvaIdx] += (end - start)
                countMeeting[minAvaIdx] += 1
                mostMeet = max(mostMeet, countMeeting[minAvaIdx])
        
        
        return countMeeting.index(mostMeet)
                
                
                
                
        
        
        
        if n > len(meetings):
            return 0
        
        meetings.sort(key=lambda x:x[0])
        
        mnHe = []
        rooms = [0] * n
        mx = 0
        
        for meeting in range(n):
            heappush(mnHe, [meetings[meeting][1], meeting])
            rooms[meeting] += 1
            mx = max(mx, rooms[meeting])
        
        
        for meeting in range(n, len(meetings)):
            a, b = meetings[meeting]
            c, i = heappop(mnHe)
            
            rooms[i] += 1
            mx = max(mx, rooms[i])
            dif = b - a
            heappush(mnHe, [c + dif, i])
        

        print(mnHe)
        return rooms.index(mx)
        
        
