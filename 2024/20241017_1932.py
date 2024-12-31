# 1932: 정수 삼각형
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: International Olympiad in Informatics (IOI) 1994 Day 1 1번
# 알고리즘 분류: 다이나믹 프로그래밍

# 1. 삼각형의 크기 n 입력 (1 ≤ n ≤ 500)
# 2. n개의 줄에 걸쳐 정수 삼각형 입력
# 3. 왼쪽 위 또는 바로 위에서 내려오는 경우 중 더 큰 수를 이전 수에 더함
# [점화식] dp[i][j] = dp[i][j] + max(dp[i - 1][j - 1], dp[i - 1][j])
# 4. dp 테이블의 n-1번째 원소 중 최대값을 출력

import sys
input = sys.stdin.readline

n = int(input())
dp = []

for _ in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i + 1):
        # 왼쪽 위에서 내려올 때
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i - 1][j - 1]

        # 오른쪽 위에서 내려올 때
        if j == i:
            up = 0
        else:
            up = dp[i - 1][j]

        dp[i][j] = dp[i][j] + max(up_left, up)

print(max(dp[n - 1]))
