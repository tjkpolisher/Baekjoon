# 16395: 파스칼의 삼각형
# 출처: 2018 홍익대학교 컴퓨터공학과 코딩대회 B번
# 알고리즘 분류: 수학/다이나믹 프로그래밍/조합론

# 1. 정수 n, k 입력 (1 ≤ k ≤ n ≤ 30)
# 2. 2차원 dp 테이블 생성
# 3. dp[1][1] = 1로 초기화
# 4. 다음 행으로 넘어갈 때 맨 처음과 맨 끝 원소는 1
# 5. 이외의 원소들의 점화식: dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
# 6. dp[n][k] 출력

n, k = map(int, input().split())
dp = [[0] * (n + 1) for _ in range(n + 1)]

dp[1][1] = 1
for i in range(2, n + 1):
    dp[i][1] = 1
    dp[i][i] = 1
    for j in range(2, i):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

print(dp[n][k])
