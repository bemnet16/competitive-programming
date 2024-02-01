class Solution(object):
    def countAndSay(self, n):
        
        def say(n):
            temp = []
            i = 0
            while i < len(n):
                j = i
                count = 1
                while j < len(n) - 1 and n[j] == n[j + 1]:
                    count += 1
                    j += 1
                temp.append(str(count))
                temp.append(n[j])
                i = j + 1
                
            return "".join(temp)
            
            
            
            
        res = "1"
        for i in range(1,n):
            res = say(res)
        
        return res