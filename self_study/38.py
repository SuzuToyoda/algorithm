# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_ai
# input
# 10 5
# 8 6 9 1 2 1 10 100 1000 10000
# 2 3
# 1 4
# 3 9
# 6 8
# 1 10



n, q = map(int, input().split())

li = list(map(int, input().split()))
l_ = [0]
for i in range(len(li)):
    l_.append(l_[i] + li[i])
for query in range(q):
    l, r = map(int, input().split())

    print(l_[r] - l_[l - 1])
