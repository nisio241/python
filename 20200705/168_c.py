import math

a, b, h, m = map(int, input().split())
h_angle = (360 * h / 12) + 30 * m / 60
m_angle = 360 * m / 60
angle = abs(h_angle - m_angle)
aa = a * a + b * b - 2 * a * b * math.cos(math.radians(angle))
print(math.sqrt(aa))

