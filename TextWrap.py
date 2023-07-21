import textwrap

def wrap(string, max_width):
    idx=0
    res=[]
    while idx<len(string):
        j=0
        while j<max_width and idx<len(string):
            res.append(string[idx])
            idx+=1
            j+=1
        res.append('\n')
    res.pop()
    return "".join(res)
        

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
