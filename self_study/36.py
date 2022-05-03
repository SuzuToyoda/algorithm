import math

a, b, h, m = map(int, input().split())
hr = math.radians((h * 60 + m) * 0.5)
mr = math.radians(m * 6)
h_ = (a * math.sin(hr), a * math.cos(hr))
m_ = (b * math.sin(mr), b * math.cos(mr))

d = ((h_[0] - m_[0]) ** 2 + (h_[1] - m_[1]) ** 2) ** (1 / 2)
print(d)