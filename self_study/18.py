n = int(input())
l = list(map(int, input().split()))

d = {}

for i in range(n):
    try:
        d[l[i]] += 1
    except:
        d[l[i]] = 1
l_ = list(d.keys())
ans = 0
for k in d.keys():
    if k in l_:
        y = 500 - k
        ans += d[y] * d[k]
        del l_[l_.index(k)]
        del l_[l_.index(y)]
    else:
        continue

print(ans)
