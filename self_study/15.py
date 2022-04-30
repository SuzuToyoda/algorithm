def dev(a, b):
    if a > b:
        r = a % b
        d = b
    else:
        r = b % a
        d = a
    return r, d


def you(r, d):
    a, b = dev(r, d)
    if a == 0:
        print(b)
    else:
        you(a, b)


a, b = map(int, input().split())
you(a, b)
