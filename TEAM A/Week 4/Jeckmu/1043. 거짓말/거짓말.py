from collections import deque

N, M = map(int, input().split())
T = [*map(int, input().split())]
T_num = T[0]    # 진실을 아는 사람 수
T = T[1:]       # 진실을 아는 사람들의 번호 리스트

T = set(T)

result = 0
parties = deque()

for _ in range(M):
    A = set([*map(int, input().split())][1:])
    # 진실을 아는 사람이 있는 파티의 사람들은 모두 진실을 알게 되는 것(진실을 들으므로, 다음 번에 거짓을 들으면 들통남.)
    if len(T.intersection(A)) >= 1:
        T = T.union(A)
    else:
        parties.append(A)

for _ in range(len(parties)):
    for _ in range(len(parties)):
        p = parties.popleft()
        if len(T.intersection(p)) >= 1:
            T = T.union(p)
        else:
            parties.append(p)


for party in parties:
    if len(T.intersection(party)) == 0:
        result += 1

print(result)