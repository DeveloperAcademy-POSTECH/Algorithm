#백준, 19532.수학은 비대면 강의입니다.
# 풀이 1
a,b,c,d,e,f = map(int, input().split())

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x + b*y == c and d*x + e*y == f:
            break
    if a*x + b*y == c and d*x + e*y == f:
        break

print(x, y)

# 풀이 1-1
a,b,c,d,e,f = map(int, input().split())
found = False

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x + b*y == c and d*x + e*y == f:
            found = True
            break
    if found:
        break

print(x, y)