def solution(alp, cop, problems):
    max_alp_req, max_cop_req = -1, -1
    
    for alp_req, cop_req, _, _, _ in problems:
        max_alp_req = max(max_alp_req, alp_req)
        max_cop_req = max(max_cop_req, cop_req)
        
    # print(max_alp_req, max_cop_req)

    # dp[i][j] = 알고력이 i, 코딩력이 j가 되기 위해 필요한 최소 코스트
    dp = [[int(1e9) for _ in range(max_cop_req + 1)] for _ in range(max_alp_req + 1)]
    
    # dp 시작점 초기화
    alp = min(alp, max_alp_req)
    cop = min(cop, max_cop_req)
    dp[alp][cop] = 0
    
    for i in range(alp, max_alp_req + 1):
        for j in range(cop, max_cop_req + 1):
            if i < max_alp_req:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            if j < max_cop_req:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)
            
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    new_alp = min(i + alp_rwd, max_alp_req)
                    new_cop = min(j + cop_rwd, max_cop_req)
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[i][j] + cost)
        
    return dp[max_alp_req][max_cop_req]
