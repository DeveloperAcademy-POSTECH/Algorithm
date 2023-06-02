nums = [*map(int, input().split())]

# dp[i][left][right] = Minimum of Sum of power - [ith][left foot][right foot]
dp = [[[4*len(nums) for _ in range(5)] for _ in range(5)]
      for _ in range(len(nums))]
dp[0][0][0] = 0


def po(a, b):
    if a == 0:
        return 2
    elif a == b:
        return 1
    elif abs(a-b) == 2:
        return 4
    else:
        return 3


for i in range(len(dp)-1):
    a = nums[i]
    for left in range(5):
        for right in range(5):
            dp[i+1][left][a] = min(dp[i+1][left][a], dp[i]
                                   [left][right] + po(right, a))
            dp[i+1][a][right] = min(dp[i+1][a][right],
                                    dp[i][left][right] + po(left, a))

print(min(map(min, dp[len(dp)-1])))