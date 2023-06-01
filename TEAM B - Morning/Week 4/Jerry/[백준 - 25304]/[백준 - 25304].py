#25304 백준

x = int(input())
sum = 0

for _ in range(int(input())):
    a, b = map(int, input().split())
    sum += a * b

print("Yes") if sum == x else print("No")