# 2156: 포도주 시식
# 알고리즘 분류: 다이나믹 프로그래밍

# 1. 포도주 잔의 개수 n 입력 (1 ≤ n ≤ 10,000)
# 2. n개의 줄에 걸쳐 각 포도주 잔에 담긴 포도주의 양 입력 (1000 이하의 음이 아닌 정수)
# 3. dp 리스트 생성 - dp[i]는 i번째 잔까지 고려했을 때 최대로 마실 수 있는 포도주의 양
# 4. dp[i]의 값은 다음 세 가지 경우 중 최댓값:
# 4-1. i번째 포도주를 마시지 않는 경우: dp[i-1]
# 4-2. i번째 포도주를 마시고 i-1번째는 마시지 않는 경우: dp[i-2] + wine[i]
# 4-3. i번째와 i-1번째 포도주를 마시고 i-2번째는 마시지 않는 경우: dp[i-3] + wine[i-1] + wine[i]
# 5. dp 리스트의 n번째 요소 출력

import sys
input = sys.stdin.readline

n = int(input())
wine = [0]  # 인덱스를 1부터 시작하기 위해 0을 추가
for _ in range(n):
    wine.append(int(input()))

dp = [0] * (n + 1)

# 초기값 설정
if n >= 1:
    dp[1] = wine[1]
if n >= 2:
    dp[2] = wine[1] + wine[2]
if n >= 3:
    dp[3] = max(wine[1] + wine[3], wine[2] + wine[3], wine[1] + wine[2])

# 네 번째 잔부터 dp 진행
for i in range(4, n + 1):
    dp[i] = max(
        dp[i-1],  # i번째 포도주를 마시지 않는 경우
        dp[i-2] + wine[i],  # i번째 포도주를 마시고 i-1번째는 마시지 않는 경우
        dp[i-3] + wine[i-1] + wine[i]  # i번째와 i-1번째 포도주를 마시고 i-2번째는 마시지 않는 경우
    )

print(dp[n])
