# 11660: 구간 합 구하기 5
# 알고리즘 분류: 다이나믹 프로그래밍/누적 합

# 1. 표의 크기 N과 합을 구해야 하는 횟수 M 입력 (1 ≤ N ≤ 1024, 1 ≤ M ≤ 100,000)
# 2. N개의 줄에 걸쳐 표의 각 행을 입력
# 3. M개의 줄에 걸쳐 네 개의 정수 x1, y1, x2, y2 입력 (x1 ≤ x2, y1 ≤ y2)
# 4. 2차원 누적합을 계산
# 4-1. 어떤 행 또는 어떤 열에 대한 누적 합은 1차원 누적합과 동일
# 4-2. 2차원 누적합 계산 시, 위와 왼쪽의 누적합을 표의 현위치의 값에 더하고, 중복되는 영역의 수를 빼서 구함
# 5. 2차원 누적합 테이블에서 아래 공식을 이용해 2차원 구간 합 계산
# ans = prefix[x2][y2] - prefix[x1 - 1][y2] - prefix[x2][y1 - 1] + prefix[x1 - 1] + prefix[y1 - 1]

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [[0] for _ in range(N + 1)]
grid[0] = [0] * (N + 1)
for i in range(1, N + 1):
    grid[i].extend(list(map(int, input().split())))

prefix = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for y in range(N):
    for x in range(N):
        prefix[x + 1][y + 1] = prefix[x][y + 1] + prefix[x + 1][y] - prefix[x][y] + grid[x + 1][y + 1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    ans = prefix[x2][y2] - prefix[x1 - 1][y2] - prefix[x2][y1 - 1] + prefix[x1 - 1][y1 - 1]
    print(ans)
