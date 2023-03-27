def firstPalindrome(self, words):
        for i in words:
            s = 0
            l = len(i) - 1
            for j in range(len(i)):
                if i[j] != i[l - j]:
                    break
                if j == (l - j) or j - 1 == (l - j):
                    return i
        return ""
