# import sys

# k, n = map(int, sys.stdin.readline().split())
# arr = []

# for i in range(k):
#     arr.append(int(input()))

# result = max(arr)//2
# a = 1000000
# count = []

# while result != 0:
#     for i in arr:
#         count.append(int(i/result))
#     if sum(count) == n:
#         if a > result:
#             a = int(result)
#     elif sum(count) > n:
#         break
#     else:
#         count = []
#     result -=1

# print(a)


import sys

k, n = map(int, sys.stdin.readline().split())
arr = []

for i in range(k):
    arr.append(int(input()))

start = 1
end = max(arr)

while (start <= end):
    mid = (start + end) // 2
    cnt = 0
    for i in range(k):
        cnt += arr[i] // mid
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)