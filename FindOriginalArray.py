class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2:
            return []
        chgArr=[]
        
        temp=Counter(changed)
        changed.sort()
        for number in changed:
            if number==0 and temp[number]>=2:
                chgArr.append(number)
                temp[number]-=2
            if number>0  and temp[number] and temp[2*number]:
                chgArr.append(number)
                temp[number]-=1
                temp[2*number]-=1
        if len(chgArr)==len(changed)//2:
            return chgArr
        return []
