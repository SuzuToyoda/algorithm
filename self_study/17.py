n = int(input())
l = list(map(int, input().split()))


def div(a_, b_):
    if a_ > b_:
        return b_, a_ % b_
    else:
        return a_, b_ % a_


def max(x, y):
    def com(a_, b_):
        a, b = div(a_, b_)
        if b == 0:
            return a
        else:
            return com(a, b)
    c = com(x, y)
    return c * (x // c) * (y // c)


ans = max(l[0], l[1])

for i in range(2, n):
    ans = max(ans, l[i])
print(ans)
