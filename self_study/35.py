n = int(input())
p = []
for i in range(n):
    x, y = map(int, input().split())
    p.append((x, y))

ans = ((p[0][0] - p[1][0]) ** 2 + (p[0][1] - p[1][1]) ** 2) ** (1 / 2)

for i in range(n):
    for j in range(i + 1, n):
        d = ((p[i][0] - p[j][0]) ** 2 + (p[i][1] - p[j][1]) ** 2) ** (1 / 2)
        if d <= ans:
            ans = d

print(ans)
