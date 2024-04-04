class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        
        primes = set()
        sieve_matrix = [1 for _ in range(n)]
        
        for i in range(2, (n)):
            
            if sieve_matrix[i] == 1:
                primes.add(i)
                sieve_matrix[i] == 0
                
                tmp = i * i
                while tmp < (n):
                    sieve_matrix[tmp] = 0
                    tmp += i
        
        
        
        answer = []
        
        for num in range(1, n // 2 + 1):
            
            if num in primes and (n - num) in primes:
                answer.append([num, (n - num)])
        
        return answer
        