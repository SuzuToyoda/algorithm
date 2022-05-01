n, r = map(int, input().split())
ue = n
shita = 1

for i in range(1, r):
    ue *= (n - i)
    shita *= i

shita *= r

print(ue // shita)
