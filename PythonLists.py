if __name__ == '__main__':
    N = int(input())
    ls = []
    for i in range(N):
        inp = input().split()
        inst = inp[0]
        if inst == "insert":
            ls.insert(int(inp[1]), int(inp[2]))
        elif inst == "print":
            print(ls)
        elif inst == "remove":
            ls.remove(int(inp[1]))
        elif inst == "append":
            ls.append(int(inp[1]))
        elif inst == "sort":
            ls.sort()
        elif inst == "pop":
            ls.pop()
        elif inst == "reverse":
            ls.reverse()
