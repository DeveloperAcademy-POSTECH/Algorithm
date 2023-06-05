n = int(input())    
arr = []
temp_sum = set()
for i in range(n):
    arr.append(int(input()))
for i in range(n):
    for j in range(n):
        temp_sum.add(arr[i]+arr[j])
arr.sort(reverse=True)
def solvethe2295():
    for i in range(n):
        for k in range(i, n):
            if(arr[i]-arr[k] in temp_sum):
                return (arr[i])
print(solvethe2295())