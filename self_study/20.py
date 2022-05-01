n = int(input())
l = list(map(int, input().split()))
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for g in range(j + 1, n):
            for u in range(g + 1, n):
                for p in range(u + 1, n):
                    if l[i] + l[j] + l[g] + l[u] + l[p] == 1000:
                        ans += 1
                    else:
                        continue

print(ans)