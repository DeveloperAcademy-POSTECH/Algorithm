N, L = map(int, input().split())

M = []
for _ in range(N):
    M.append(list(map(int, input().split())))

result = 0

install = []
for _ in range(N):
    install.append([False]*N)

# 가로(행)의 가능한 길
for r, row in enumerate(M):
    flag = True
    for i in range(N-1):
        if abs(row[i]-row[i+1]) > 1:
            flag = False
            break

        if row[i] == row[i+1]+1:    # 왼쪽이 크면
            for k in range(1, L+1):
                # index out of range
                if not 0 <= i+k < N:
                    flag = False
                    break
                # 이후 L개동안 같은 숫자가 아니라면
                if row[i] != row[i+k]+1 or install[r][i+k]:
                    flag = False
                    break

            if flag:
                for k in range(1, L+1):
                    install[r][i+k] = True

        if row[i] == row[i+1]-1:    # 오른쪽이 크면
            for k in range(0, L):
                # index out of range
                if not 0 <= i-k < N:
                    flag = False
                    break
                # 이전 L개가 같은 숫자가 아니라면
                if row[i-k] != row[i+1]-1 or install[r][i-k]:
                    flag = False
                    break

            if flag:
                for k in range(0, L):
                    install[r][i-k] = True

    if flag:
        result += 1

install = []
for _ in range(N):
    install.append([False]*N)

# 세로(열)의 가능한 길
for r in range(N):
    row = []
    for k in range(N):
        row.append(M[k][r])

    flag = True
    for i in range(N-1):
        if abs(row[i]-row[i+1]) > 1:
            flag = False
            break
        if row[i] == row[i+1]+1:    # 왼쪽이 크면
            for k in range(1, L+1):
                # index out of range
                if not 0 <= i+k < N:
                    flag = False
                    break
                # 이후 L개동안 같은 숫자가 아니라면
                if row[i] != row[i+k]+1 or install[i+k][r]:
                    flag = False
                    break

            if flag:
                for k in range(1, L+1):
                    install[i+k][r] = True

        if row[i] == row[i+1]-1:    # 오른쪽이 크면
            for k in range(0, L):
                # index out of range
                if not 0 <= i-k < N:
                    flag = False
                    break
                # 이전 L개가 같은 숫자가 아니라면
                if row[i-k] != row[i+1]-1 or install[i-k][r]:
                    flag = False
                    break

            if flag:
                for k in range(0, L):
                    install[i-k][r] = True

    if flag:
        result += 1

print(result)