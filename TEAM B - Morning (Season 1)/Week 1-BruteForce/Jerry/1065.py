num = int(input())
total = 0

for i in range(1, num + 1):
    if i < 100:
        total += 1
    else:
        num_arr = list(map(int, str(i)))
        if num_arr[0] - num_arr[1] == num_arr[1] - num_arr[2]:
            total += 1

print(total)