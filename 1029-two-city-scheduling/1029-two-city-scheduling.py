class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        cost_difference = []
        for i in range(len(costs)):
            difference = costs[i][0] - costs[i][1]
            cost_difference.append([i, difference])
        
        cost_difference.sort(key = lambda x:x[1])
        
        answer = 0
        for i in range(len(costs)//2):
            answer += costs[cost_difference[i][0]][0]
            answer += costs[cost_difference[-i - 1][0]][1]
        
        return answer
        