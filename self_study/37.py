x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x4, y4 = map(int, input().split())
s = ((x1 - x2) * (y3 - y1)) - ((y1 - y2) * (x3 - x1))
t = ((x1 - x2) * (y4 - y1)) - ((y1 - y2) * (x4 - x1))

if s * t < 0:
    print("No")
else:
    print("Yes")
