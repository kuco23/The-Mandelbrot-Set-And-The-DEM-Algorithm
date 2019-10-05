PIXELS = 1000
RANGEX = (-2, 2)
RANGEY = (-2, 2)
COLOR = (255, 111, 204)

PPM_FILE = 'mandelbrot.ppm'
PPM_HEADER = ['P3\n', f'{PIXELS} {PIXELS}\n', '255\n']

iterlim = 40
iterFun = lambda z, c: z * z + c

def pointConvergance(point):
    z, count = complex(0, 0), 0
    eps = max(2, abs(point))
    while count < iterlim and abs(z) <= eps:
        z = iterFun(z, point)
        count += 1
    return count

def setPoint(i, j):
    (a, b), (c, d) = RANGEX, RANGEY
    x = i / PIXELS * (b - a) + a
    y = j / PIXELS * (d - c) + c
    return complex(x, y)

open(PPM_FILE, 'a').close()
file = open(PPM_FILE, 'w', encoding='ascii')
for h in PPM_HEADER: file.write(h)

for j in range(PIXELS):
    file.write('\n')
    for i in range(PIXELS):
        point = setPoint(i, j)
        count = pointConvergance(point)
        base = (255 * count) // iterlim * (count < iterlim)
        r, g, b = map(lambda c: (c / 255) * base, COLOR)
        file.write(f'{r} {g} {b}  ')

file.flush()
file.close()