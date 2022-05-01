n = int(input())
l = list(map(int, input().split()))
d = {}
ans = 0
for i in range(n):
    try:
        d[l[i]] += 1
    except:
        d[l[i]] = 1
l = list(d.keys())
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] + l[j] == 100000:
            ans += d[l[i]] * d[l[j]]
            d[i] = 0
            d[j] = 0
if d[50000] >= 2:
    ans += d[50000] // 2
print(ans)
