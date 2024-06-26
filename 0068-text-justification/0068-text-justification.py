class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        ans = []
        temp = []
        word_lg = 0
        spaces = 0
        total_lg = 0
        
        for word in words:
            
            if total_lg + len(word) > maxWidth:
                
                total_lg -= spaces   # only the length of the strings
                spaces -= 1          # No of spaces between words
                tot_spaces = maxWidth - total_lg   
                
                # only one word in temp
                if spaces == 0:
                    temp.append(" " * (maxWidth - len(temp[0])))
                    ans.append("".join(temp))
                
                else:
                    q = tot_spaces // spaces
                    r = tot_spaces % spaces

                    line = []
                    for w in temp:
                        line.append(w)
                        if r > 0:
                            line.append(" " * (q + 1))
                            r -= 1
                        else:
                            line.append(" " * q)
                    line.pop()
                    ans.append("".join(line))
                 
                # hold the current word to proceed
                word_lg = len(word)
                spaces = 1
                total_lg = word_lg + spaces
                temp = [word]
                        
                
            
            else:
                temp.append(word)
                word_lg += len(word)
                spaces += 1
                total_lg = word_lg + spaces
    
    
        # handle last line words
        if temp:
            s = " ".join(temp)
            s += " " * (maxWidth - len(s))
            
        ans.append(s)
        return ans