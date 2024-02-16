class Solution:
    def bestClosingTime(self, customers: str) -> int:
        
        y_sum = [0] * len(customers)
        n_sum = [0] * len(customers)
        
        y_acc = 0
        n_acc = 0
        for i in range(len(customers)):
            
            if customers[i] == "Y":
                y_acc += 1
            else:
                n_acc += 1
                
            y_sum[i] = y_acc
            n_sum[i] = n_acc
            
            
        
        minimum_penality = float("inf")
        earliest_hour = None

        for i in range(len(customers)+1):
            
            # close on the 0th hour is equal to the sum of 'Y's
            if i == 0:
                penality = y_sum[-1]
                
            # close after the end is equal to the sum of all 'N'
            elif i == len(customers):
                penality = n_sum[-1]
                
            else:
                penality = (y_sum[-1]-y_sum[i-1])+(n_sum[i-1])
                
            if minimum_penality > penality:
                minimum_penality = penality
                earliest_hour = i
                
        return earliest_hour
                
            
            
        