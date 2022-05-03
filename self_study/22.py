n = int(input())
l = list(map(int, input().split()))
l_ = [0] * 100001
ans = 0
for i in range(n):
    l_[l[i]] += 1
for i in range(100001):
    if i == 50000:
        ans += (l_[i] * (l_[i] - 1)) // 2
    else:
        if l_[i] != 0:
            ans += l_[i] * l_[100000 - i]
            l_[100000 - i] = 0

print(ans)
