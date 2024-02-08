class Solution(object):
    def corpFlightBookings(self, bookings, n):
        flight = [0] * n
        
        for f,l,s in bookings:
            flight[f - 1] += s
            if l < n:
                flight[l] -= s
        
        for i in range(1,n):
            flight[i] += flight[i - 1]
        
        return flight
            