def add_digits(num):
    total = 0
    for digit in str(num):
        total += int(digit)
    return total + num

list1 = [num for num in range(1, 10001)]

for i in range(1,9973):
    a = add_digits(i)
    if a in list1:
        list1.remove(a)

for i in list1:
    print(i)


