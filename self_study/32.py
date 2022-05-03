n, x = map(int, input().split())
l = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if l[i] == x:
        print("Yes")
        cnt += 1
        break
if cnt != 1:
    print("No")
