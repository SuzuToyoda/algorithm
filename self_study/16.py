n = int(input())
l = list(map(int, input().split()))

def div(_a, _b):
    if _a > _b:
        r = _a % _b
        return _b, r
    else:
        r = _b % _a
        return _a, r


def rep(a, b):
    b_, r = div(a, b)
    if r != 0:
        return rep(b_, r)
    else:
        return b_


com_div = rep(l[0], l[1])

for i in range(2, n):
    com_div = rep(l[i], com_div)

print(com_div)
