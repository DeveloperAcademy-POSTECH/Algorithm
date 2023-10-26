num_people = int(input())
arr = list(map(int, input().split()))
arr.sort()

def min_time():
    for i in range(1,len(arr)):
        arr[i] = arr[i] + arr[i-1]

    return sum(arr)

print(min_time())