class Solution(object):
    def numberToWords(self, num):
        if num==0: return 'Zero'
        r=[]
        mi,th=False,False
        
        n={0:'',
           1:'One',
           2:'Two',
           3:'Three',
           4:'Four',
           5:'Five',
           6:'Six',
           7:'Seven',
           8:'Eight',
           9:'Nine'}
        
        el={10:'Ten',
            11:"Eleven",
            12:'Twelve',
            13:"Thirteen",
            14:"Fourteen",
            15:"Fifteen",
            16:"Sixteen",
            17:"Seventeen",
            18:"Eighteen",
            19:"Nineteen"}
        
        ha={2:"Twenty",
            3:"Thirty",
            4:"Forty",
            5:"Fifty",
            6:"Sixty",
            7:"Seventy",
            8:"Eighty",
            9:"Ninety"}
        
        b=num//1000000000
        num=num-(1000000000*b)
        if b:
            s=n[b]+' Billion '
            r.append(s)
        m=num//1000000
        if m:
            mi=True
        num=num-(1000000*m)
        mt=m//100
        m=m-(100*mt)
        if mt>0:
            s=n[mt]+' Hundred '
            r.append(s)
        for j in range(1,-1,-1):
            if m>=10 and m<20:
                r.append(el[m])
                break
            elif m>=20:
                r.append(ha[m//10]+' ')
                m=m-((m//10**j)*10**j)
                continue
            else:
                mt=m//10**j
                r.append(n[mt])
                m=m-(mt*10**j)
        if mi:
            r.append(' Million ')

        t=num//1000
        if t:
            th=True
        num=num-(1000*t)
        tt=t//100
        t=t-(100*tt)
        if tt>0:
            s=n[tt]+' Hundred '
            r.append(s)
        for j in range(1,-1,-1):
            if t>=10 and t<20:
                r.append(el[t])
                break
            elif t>=20:
                r.append(ha[t//10]+' ')
                t=t-((t//10**j)*10**j)
                continue
            else:
                tt=t//10**j
                r.append(n[tt])
                t=t-(tt*10**j)
        if th:
            r.append(' Thousand ')

        h=num
        ht=h//100
        h=h-(100*ht)
        if ht>0:
            s=n[ht]+' Hundred '
            r.append(s)
        for j in range(1,-1,-1):
            if h>=10 and h<20:
                r.append(el[h])
                break
            elif h>=20:
                r.append(ha[h//10]+' ')
                h=h-((h//10**j)*10**j)
                continue
            else:
                ht=h//10**j
                r.append(n[ht])
                h=h-(ht*10**j)
        r="".join(r)
        r=" ".join(r.split())
        return r
