def searchArr(array = []):
    count1 = 0
    count2 = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if (i + j) % 2 == 0:
                if array[i][j] != 'B':
                    count1 += 1
                if array[i][j] != 'W':
                    count2 += 1
            else:
                if array[i][j] != 'W':
                    count1 += 1
                if array[i][j] != 'B':
                    count2 += 1
    if count1 < count2:
        return count1
    else:
        return count2


row, col = map(int,input().split())
array = [list(input()) for _ in range(row)]
arr1 = []

if (row <= 8) & (col <= 8):
    count = searchArr(array)
    arr1.append(count)
else:
    for i in range(row - 7):
        for j in range(col - 7):
            array1 = [row[j:8+j] for row in array[i:8+i]]
            count = searchArr(array1)
            arr1.append(count)

print("{}".format(min(arr1)))







# Create a 10x13 array filled with zeros
# array_10x13 = [[j for j in range(13)] for i in range(10)]

# # Select an 8x8 subset of the array starting from the top-left corner
# array_8x8 = [row[:8] for row in array_10x13[:8]]

# # Print the resulting array
# for row in array_8x8:
#     print(row)





# 8 8
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBBBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW
