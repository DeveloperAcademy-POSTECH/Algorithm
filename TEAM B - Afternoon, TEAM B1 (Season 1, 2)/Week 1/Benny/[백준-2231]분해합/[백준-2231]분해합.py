#백준.2231.분해합

n = int(input())
num = 1
while num < n:
    decomp_sum = num + sum(map(int, list(str(num))))
    if decomp_sum == n:
        break
    num += 1
        
num = 0 if num == n else num
print(num)