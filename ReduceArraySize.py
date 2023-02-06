class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        c = Counter(arr)
        lg = len(arr) // 2
        result = 0
        temp = 0

        n_a = [i for i in c.values()]
        n_a.sort(reverse=True)
        for j in n_a:
            temp += j
            result += 1 
            if temp >= lg : 
                break           
        return result  
