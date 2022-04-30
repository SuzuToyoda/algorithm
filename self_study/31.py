n = int(input())
l = list(map(int, input().split()))
d = [0] * (n + 1)
d[1] = l[0]
d[2] = l[1]
for i in range(2, n + 1):
    d[i] = max(d[i - 2] + l[i - 1], d[i - 1])
print(d[n])
