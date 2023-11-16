H, W = map(int, input().split())

blocks = list(map(int, input().split()))

result = 0
for i in range(1, len(blocks)-1):
    left = max(blocks[:i])
    right = max(blocks[i:])
    
    rainAmount = min(left, right) - blocks[i]
    if rainAmount > 0:
        result += rainAmount

print(result)