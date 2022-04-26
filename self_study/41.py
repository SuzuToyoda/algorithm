#https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_al

t = int(input())
n = int(input())
l_ = [0] * (t+1)
for i in range(n):
    l, r = map(int, input().split())
    l_[l] += 1
    l_[r] -= 1
ans = 0
for i in range(t):
    ans += l_[i]
    print(ans)
