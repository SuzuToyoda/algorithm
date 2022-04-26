# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_aj

n, q = map(int, input().split())
l_ = [0] * (n + 1)
for i in range(q):
    l, r, x = map(int, input().split())
    l_[l - 1] += x
    l_[r] -= x
ans = ""
for i in range(1, len(l_) - 1):
    if l_[i] < 0:
        ans += ">"
    elif l_[i] > 0:
        ans += "<"
    else:
        ans += "="
print(ans)
