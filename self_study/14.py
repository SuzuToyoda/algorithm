n = int(input())
l = []


def sep(n):
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return i, n // i
    return False


def so_in(n):
    if sep(n) == False:
        l.append(n)
    else:
        x, y = sep(n)
        l.append(x)
        so_in(y)
    return l


ans = map(str, sorted(so_in(n)))
print(' '.join(ans))
