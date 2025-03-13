# 19621: 회의실 배정 2
# 알고리즘 분류: 다이나믹 프로그래밍/브루트포스 알고리즘

# 1. 회의의 수 N 입력 (1 ≤ N ≤ 25)
# 2. N개의 줄에 걸쳐 회의 시작 시간과 끝나는 시간, 회의 인원 입력
# [보충설명] 임의의 회의 K(1≤ K ≤ N)는 회의 K − 1과 회의 K + 1과는 회의 시간이 겹치고 다른 회의들과는 회의 시간이 겹치지 않음.
# [보충설명] 모든 회의 시작 및 끝 시간은 2^31 - 1 이하의 자연수 또는 0.
# [보충설명] 모든 회의의 시작 시간과 끝 시간은 서로 다름.
# [보충설명] 회의 인원은 1000 이하의 자연수.
# 3. 길이 N의 dp 테이블을 생성하고 첫번째 원소를 첫 번째 회의의 인원으로 초기화
# 4. 점화식: dp[i] = max(dp[i - 1], dp[i - 2] + meetings[i][2])
# 5. dp[-1] 출력

import sys
input = sys.stdin.readline

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * N
dp[0] = meetings[0][2]

for i in range(1, N):
    dp[i] = max(dp[i - 1], dp[i - 2] + meetings[i][2])

print(dp[-1])
