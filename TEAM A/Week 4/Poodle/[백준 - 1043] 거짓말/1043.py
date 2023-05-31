# 백준 1043번: 거짓말

import sys

input = sys.stdin.readline

# N, M <= 50
N, M = map(int, input().rstrip().split())

know_truth = [False for _ in range(N + 1)]

len_known, *knowns = map(int, input().rstrip().split())
for person in knowns:
    know_truth[person] = True

parent = [i for i in range(N + 1)]

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x

def union(a, b):
    A = find(a)
    B = find(b)

    if A > B:
        A, B = B, A

    parent[B] = A

    if know_truth[A] or know_truth[B]:
        know_truth[A] = True
        know_truth[B] = True

parties = []
for _ in range(M):
    len_participant, *participants = map(int, input().rstrip().split())
    parties.append(participants)
    
    if len_participant == 1: continue

    for idx in range(1, len_participant):
        if find(participants[idx]) != find(participants[idx - 1]):
            union(participants[idx], participants[idx - 1])

# print(parent)
# print(know_truth)
answer = 0

for party in parties:
    available_lie = True

    for member in party:
        if know_truth[find(member)]:
            available_lie = False
            break

    if available_lie: answer += 1

print(answer)
