class Solution(object):
    def minWindow(self, s, t):
        
        if len(t) > len(s):
            return ""
        
        ls,lt = len(s),len(t)
        st = set(t)
        dt = {}
        for char in t:
            dt[char] = dt.get(char,0) + 1
        
            
        res = ""
        sr = set(s[0:lt])
        lr = float("inf")
        
        dr = {}
        for char in s[0:lt]:
            dr[char] = dr.get(char,0) + 1

        i,j = lt - 1,0
        while i < ls:
            if st.issubset(sr):
                isSub = all(dr.get(key,0) >= val for key,val in dt.items())
                if isSub:
                    if dr[s[j]] >= 2:
                        dr[s[j]] -= 1
                    elif dr[s[j]] == 1:
                        del dr[s[j]]
                        sr.discard(s[j])
                    
                    if (i - j) < lr:
                        res = s[j:i + 1]
                        lr = i - j
                    j += 1
                    
                else:
                    i += 1
                    if i < ls:
                        dr[s[i]] = dr.get(s[i],0) + 1
                        sr.add(s[i])
                
            else:
                i += 1
                if i < ls:
                    dr[s[i]] = dr.get(s[i],0) + 1
                    sr.add(s[i])
        
        return res
                
        
        
        
        
        
        
        
        
        
        
        
        
        