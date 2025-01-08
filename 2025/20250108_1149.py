# 1149: RGB거리
# 알고리즘 분류: 다이나믹 프로그래밍

# 1. 집의 수 N 입력 (2 ≤ N ≤ 1,000)
# 2. N개의 줄에 걸쳐 각 집을 빨강/초록/파랑으로 칠하는 비용을 입력 (비용은 1000 이하의 자연수)
# 3. 2차원 dp 테이블의 첫 번째 원소에 첫 번째 집의 최소 비용을 입력
# 4. 점화식
# 4-1. dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + 현재 집 비용
# 4-2. dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + 현재 집 비용
# 4-3. dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + 현재 집 비용
# 5. dp[N - 1]의 최소값을 출력

import sys
input = sys.stdin.readline

N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N)]
dp[0] = costs[0]

for i in range(1, N):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]

print(min(dp[N - 1]))
