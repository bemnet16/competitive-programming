class Solution:
    def bestClosingTime(self, customers):
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
        
        mini = float("inf")
        idx = None

        for j in range(len(customers)+1):
            if j == 0:
                cur = y_sum[-1]
            elif j == len(customers):
                cur = n_sum[-1]
            else:
                cur = (y_sum[-1]-y_sum[j-1])+(n_sum[j-1])
                
            if mini > cur:
                mini = cur
                idx = j
                
        return idx
                
            
            
        