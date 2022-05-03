n = int(input())
l = list(map(int, input().split()))
ans = []
left = []
right = []
ave = sum(l) // n
for i in range(n):
    if l[i] <= ave:
        left.append(l[i])
    else:
        right.append(l[i])


