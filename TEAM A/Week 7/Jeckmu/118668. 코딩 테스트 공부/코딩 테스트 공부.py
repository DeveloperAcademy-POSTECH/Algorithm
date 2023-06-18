def solution(alp, cop, problems):
    INF = 10**9
    max_alp, max_cop = 0, 0

    for p in problems:
        max_alp = max(max_alp, p[0])
        max_cop = max(max_cop, p[1])
        
    # 런타임 에러 해결    
    if alp > max_alp:
        alp = max_alp
    if cop > max_cop:
        cop = max_cop

    dp = [[INF]*(max_cop+1) for _ in range(max_alp+1)]
    dp[alp][cop] = 0

    # 현재 alp부터 필요 alp까지, 현재 cop부터 필요 cop까지의 dp 배열을 memoization을 이용해 채워 나감.
    for i in range(alp, max_alp+1):
        for j in range(cop, max_cop+1):
            if i < max_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            if j < max_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)

            for p in problems:
                if i >= p[0] and j >= p[1]:
                    alp_n = i+p[2]
                    cop_n = j+p[3]
                    if alp_n > max_alp:
                        alp_n = max_alp
                    if cop_n > max_cop:
                        cop_n = max_cop

                    dp[alp_n][cop_n] = min(dp[alp_n][cop_n], dp[i][j]+p[4])
                    
    return dp[max_alp][max_cop]