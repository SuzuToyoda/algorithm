n = int(input())
l = list(map(int, input().split()))
m = int(input())
l_ = [0]

for i in range(n - 1):
    l_.append(l[i] + l_[i])
# [0, 8, 14, 23]
len = 0
pre = int(input())
for t in range(m - 1):
    st = int(input())
    len += abs(l_[st - 1] - l_[pre - 1])
    pre = st
print(len)
