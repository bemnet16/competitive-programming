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
                
           