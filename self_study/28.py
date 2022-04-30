# https://atcoder.jp/contests/math-and-algorithm/tasks/dp_a

n = int(input())
l = list(map(int, input().split()))
d = [0, abs(l[1] - l[0])]
for i in range(2, n):
    a_1 = d[i - 2] + abs(l[i - 2] - l[i])
    a_2 = d[i - 1] + abs(l[i - 1] - l[i])
    d.append(min(a_2, a_1))
print(d[n - 1])
