class Solution(object):
    def countVowels(self, word):
        t=0
        vowel=set({'a','e','i','o','u'})
        for i,v in enumerate(word):
            if v in vowel:
                t+=(i+1)*(len(word)-i)
        return t
      
    ### or
    
        # a=[(i+1)*(len(word)-i) for i,v in enumerate(word) if v in 'aeiou']
        # return sum(a)
                
