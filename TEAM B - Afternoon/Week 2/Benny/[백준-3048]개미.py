#https://www.acmicpc.net/problem/3048

n1, n2 = map(int, input().split())

group1 = [(True, ant) for ant in reversed(input())]
group2 = [(False, ant) for ant in input()]

cur_second = 0
target_second = int(input())

ants = group1 + group2

while cur_second < target_second:
    temp = set([])
    for i in range(len(ants)-1):
        if ants[i] not in temp and ants[i+1] not in temp and ants[i][0] and not ants[i+1][0]:
            ants[i], ants[i+1] = ants[i+1], ants[i]
            temp.add(ants[i])
            temp.add(ants[i+1])
    cur_second += 1
        
print(''.join([ant[1] for ant in ants]))