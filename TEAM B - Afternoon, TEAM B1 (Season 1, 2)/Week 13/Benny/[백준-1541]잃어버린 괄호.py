#백준-1541-잃어버린 괄호
#https://www.acmicpc.net/problem/1541

import sys, re

input = sys.stdin.readline

exp = input()
operators = re.findall(r'[\-\+]', exp)
nums = list(map(int, re.split(r'[\-\+]', exp)))

if '-' in operators:
    first_minus_idx = operators.index('-') + 1
    result = sum(nums[:first_minus_idx]) - sum(nums[first_minus_idx:])
    print(result)
else:
    result = sum(nums)
    print(result)