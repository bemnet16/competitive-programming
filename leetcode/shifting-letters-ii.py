class Solution(object):
    def shiftingLetters(self, s, shifts):
        d_ltr = {}
        l_ltr = []
        for i in range(97,123):
            d_ltr[chr(i)] = i - 97
            l_ltr.append(chr(i))
        
        res = []
        p_sum = [0] * (len(s) + 1)
        for i,j,d in shifts:
            if d == 1:
                p_sum[i] += 1
                p_sum[j + 1] -= 1
            else:
                p_sum[i] -= 1
                p_sum[j + 1] += 1
        
        for i in range(1,len(s)):
            p_sum[i] += p_sum[i - 1]
        
        for i in range(len(s)):
            idx = (d_ltr[s[i]] + (( p_sum[i]) % 26)) % 26
            res.append(l_ltr[idx])
        
        return "".join(res)