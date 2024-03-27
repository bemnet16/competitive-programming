class Solution:
    def countPrimes(self, n: int) -> int:
        
        sieve_matrix = [1 for _ in range(n)]
        count = 0
        
        for i in range(2, (n)):
            
            if sieve_matrix[i] == 1:
                count += 1
                sieve_matrix[i] == 0
                
                tmp = i * i
                while tmp < (n):
                    sieve_matrix[tmp] = 0
                    tmp += i
                    

        return count
        
        
        