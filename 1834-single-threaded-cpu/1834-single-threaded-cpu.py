class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        for idx, task in enumerate(tasks):
            task.append(idx)
        
        tasks.sort(key=lambda x:(x[0], x[1]))

        
        minHeap = [(tasks[0][1], tasks[0][2])]
        
        
        answer = []
        enqueue_time = tasks[0][0]
        i = 1
        
        while minHeap:
            
            processing_time, index = heappop(minHeap)
            answer.append(index)
            enqueue_time += processing_time
            
            if not minHeap and i < len(tasks) and tasks[i][0] > enqueue_time:
                heappush(minHeap, (tasks[i][1], tasks[i][2]))
                enqueue_time = tasks[i][0]
                i += 1
                continue
            
            
            while i < len(tasks) and tasks[i][0] <= enqueue_time:
                heappush(minHeap, (tasks[i][1], tasks[i][2]))
                i += 1
                
        
        return answer
            