
# 배열 a의 크기 n, 배열 b의 크기 m을 입력 받음
n, m = map(int, input().split())

# 배열 a의 원소를 입력 받음
a = list(map(int, input().split()))

# 배열 b의 원소를 입력받음
b = list(map(int, input().split()))

# 두 배열을 합쳐서 정렬한 결과 출력
result = sorted(A + B)
print(' '.join(map(str, result)))