# 17845: 수강 과목
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: 제1회 UNIST 알고리즘 프로그래밍 경시대회 Uni-CODE H번
# 알고리즘 분류: 다이나믹 프로그래밍/배낭 문제

# 1. 서윤이의 최대 공부시간 N, 과목 수 K 입력(1 ≤ N ≤ 10,000, 1 ≤ K ≤ 1,000)
# 2. K개의 줄에 걸쳐 과목의 중요도 I, 필요한 공부시간 T 입력해 리스트에 저장(1 ≤ I ≤ 100,000, 1 ≤ T ≤ 10,000)
# 3. 점화식: dp[i][j] = max(I + dp[i - 1][j - T], dp[i - 1][j])
# 3-1. 단, T가 j보다 클 경우는 dp[i][j] = dp[i - 1][j]
# 4. dp[K][N] 출력

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
subjects = [list(map(int, input().split())) for _ in range(K)]
subjects.insert(0, [0, 0])

dp = [[0] * (N + 1) for _ in range(K + 1)]
for i in range(K + 1):
    I, T = subjects[i]  # 중요도, 공부 시간
    for j in range(N + 1):
        if T > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j - T] + I, dp[i - 1][j])

print(dp[K][N])
