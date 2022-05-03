ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())

x1, y1 = cx - bx, cy - by
x2, y2 = ax - bx, ay - by

bc = ((x1 ** 2) + (y1 ** 2)) ** (1 / 2)
o = abs((x1 * y2) - (y1 * x2))
print(o)

print(o / bc)
