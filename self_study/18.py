n = int(input())
l = list(map(int, input().split()))
l_ = [0] * 501
ans = 0

for i in range(n):
    l_[l[i]] += 1
for i in range(500):
    ans += l_[i] * l_[500 - i]
    l_[500 - i] = 0

print(ans)
