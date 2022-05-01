n = int(input())
l = list(map(int, input().split()))

d = {1: 0, 2: 0, 3: 0}

for i in range(n):
    d[l[i]] += 1
ans = 0
for v in d.values():
    ans += v * (v - 1) // 2
print(ans)