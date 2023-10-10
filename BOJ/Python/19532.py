# ax + by = c
# dx + ey = f
a, b, c, d, e, f = map(int, input().split())

if a == 0:
    # by = c
    y = c / b
    # dx + ey = f
    x = (f - e * y) / d
elif d == 0:
    # ey = f
    y = f / e
    # ax + by = c
    x = (c - b * y) / a
elif b == 0:
    # ax = c
    x = c / a
    # dx + ey = f
    y = (f - d * x) / e
elif e == 0:
    # dx = f
    x = f / d
    # ax + by = c
    y = (c - a * x) / b
else:
    # adx + bdy = cd
    # adx + aey = af

    # (bd - ae)y = cd - af
    y = (c * d - a * f) / (b * d - a * e)
    # ax + by = c
    x = (c - b * y) / a

print(int(x), int(y))