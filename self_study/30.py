n, w = map(int, input().split())
d = [[0] * (w + 1) for i in range(n + 1)]
w_ = [0]
v_ = [0]

for i in range(n):
    w1, v1 = map(int, input().split())
    w_.append(w1)
    v_.append(v1)

for i in range(1, n + 1):
    for j in range(w+1):
        if j < w_[i]:
            d[i][j] = d[i - 1][j]
        else:
            d[i][j] = max(d[i - 1][j], d[i - 1][j - w_[i]] + v_[i])

print(max(d[n]))
