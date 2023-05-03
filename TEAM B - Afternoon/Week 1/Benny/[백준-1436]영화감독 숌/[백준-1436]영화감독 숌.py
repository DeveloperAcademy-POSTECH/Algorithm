# 백준. 1436. 영화감독 숌
n = int(input())
count = 0
num = 1

while count < n:
    if '666' in str(num):
        count += 1
    num += 1

print(num - 1)