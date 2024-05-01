# 2167: 2차원 배열의 합
# 알고리즘 분류: 구현/누적 합

# 1. 배열의 크기 N, M 입력
# 2. N개의 줄에 걸쳐 정수를 M개씩 입력
# 3. 합을 구할 부분의 개수 K 입력
# 4. 배열의 각 원소까지의 합을 저장하는 2차원 리스트 dp 생성
# 5. 미리 입력 받은 2차원 배열의 합을 바탕으로 dp의 원소에 누적 합을 계산해 대입
# 6. K개의 줄에 걸쳐 i, j, x, y 입력
# 7. dp의 배열에 해당하는 인덱스까지의 합을 출력

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]

K = int(input())
dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = array[i - 1][j - 1] + dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]

for _ in range(K):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[x][j - 1] - dp[i - 1][y] + dp[i - 1][j - 1])
