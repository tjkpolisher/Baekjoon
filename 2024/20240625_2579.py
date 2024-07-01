# 2579: 계단 오르기
# 출처: 한국정보올림피아드 시.도지역 본선 2006 초등부 4번
# 알고리즘 분류: 다이나믹 프로그래밍

# 1. 계단의 개수 입력
# 2. 한 줄에 하나씩 제일 아래에 놓인 계단부터 순서대로 각 계단에 쓰여 있는 점수 입력
# [보충설명] 계단의 개수는 300 이하의 자연수, 계단의 쓰여 있는 점수는 10000 이하의 자연수
# 3. 아래 규칙에 맞춰 계단을 오름
# 3-1. 계단은 한 번에 한 계단 씩 또는 두 계단씩 오를 수 있음.
# 3-2. 연속된 세 개의 계단을 모두 밟아서는 안 됨. 단, 시작점은 계단에 포함되지 않음.
# 3-3. 마지막 계단은 반드시 밟아야 함.
# 4. 계단을 오를 때마다 현재까지의 합계를 저장한 메모이제이션 리스트를 참고해 더 큰 값을 추가
# 4-1. dp[n] = dp[n - 3] + stairs[n - 1] + stairs[n]
# 4-2. dp[n] = dp[n - 2] + stairs[n]
# 5. 최대 점수 출력

import sys
input = sys.stdin.readline

n = int(input())
stairs = [0] * 301
for i in range(1, n + 1):
    score = int(input())
    stairs[i] = score

dp = [0] * 301
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])
for i in range(4, n + 1):
    dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])

print(dp[n])
