n = int(input())
h = list(map(int, input().split()))

if n == 2:
  print(abs(h[-1] - h[-2]))
  exit()

ans = [0] * n
ans[-2] = abs(h[-2] - h[-1])

for i in range(n - 3, -1, -1):
  ans[i] = min((abs(h[i] - h[i + 1]) + ans[i + 1]), (abs(h[i] - h[i + 2]) + ans[i + 2]))

print(ans[0])
