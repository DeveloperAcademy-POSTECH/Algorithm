def surface_area(a, b, c):
    return (a * b + b * c + a * c) * 2


n = int(input())
divisor = []
for i in range(1, n + 1):
    if n % i == 0:
        divisor.append(i)
a = 0
b = 0
c = 0
minvalue = surface_area(1, 1, n)
for i in divisor:
    for j in divisor:
        for k in divisor:
            if i * j * k == n:
                area = surface_area(i, j, k)
                if area <= minvalue:
                    a = i
                    b = j
                    c = k
                    minvalue = area
print(a, b, c)
