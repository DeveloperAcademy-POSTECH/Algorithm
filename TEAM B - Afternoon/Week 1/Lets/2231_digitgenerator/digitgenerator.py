import sys
sys.stdin = open("2231_digitgenerator/digitgenerator.txt", "r")

N = int(sys.stdin.readline())



def generate_number(n):
    for i in range(n):
        std_num = i
        num = i
        while std_num>9:
            num += std_num % 10
            std_num //= 10
        num += std_num
        if num == n:
            return i
    return 0
        
print(generate_number(N))
