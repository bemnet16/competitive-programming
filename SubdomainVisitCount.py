class Solution(object):
    def subdomainVisits(self, cpdomains):
        d={}
        for i in cpdomains:
            ful = i.split(" ")
            count,dom = ful
            e_dom = dom.split(".")
            j=0
            while j<len(e_dom):
                domain = ".".join(e_dom[j:])
                if domain in d:
                    d[domain] = d[domain] + int(count)
                else:
                    d[domain] = int(count)
                j+=1
        res = []
        for i in d:
            temp = "{} {}".format(d[i], i)
            res.append(temp)
        return res
