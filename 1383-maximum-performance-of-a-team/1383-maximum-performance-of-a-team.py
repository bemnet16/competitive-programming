class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        temp = sorted(zip(efficiency, speed), reverse=True)
        selected_sum = 0
        heap = []
        answer = 0
        
        for i in range(n):
            
            efi, speed = temp[i]
            selected_sum += speed
            answer = max(answer, selected_sum* efi)
            
            if i < k - 1:
                heappush(heap, speed)
                
            elif heap and heap[0] < speed:
                selected_sum -= heappop(heap)
                heappush(heap, speed)
            
            else:
                selected_sum -= speed
            
            
        return answer % (10**9 + 7)
