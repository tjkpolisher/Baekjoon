# 2573: 빙산
# 출처: KOI 2006 초등부 2번
# 알고리즘 분류: 구현/그래프 이론/그래프 탐색/너비 우선 탐색/깊이 우선 탐색

# 1. 이차원 배열의 행과 열의 개수를 나타내는 두 정수 N, M 입력
# [보충설명] 3 ≤ N,M ≤ 300
# 2. N개의 줄에 걸쳐 배열의 각 행을 나타내는 M개의 정수를 입력받아 행렬에 배치
# [보충설명] 각 칸의 값은 0 이상 10 이하, 1 이상의 정수가 들어가는 칸은 10,000개 이하
# [보충설명] 배열의 첫 번째 행과 열, 마지막 행과 열은 항상 0으로 채워짐.
# 3. 행을 배치할 때 0이 아닌 칸의 좌표를 별도로 분리
# 4. 시간을 0으로 초기화
# 5. 각 시간마다 다음의 과정 반복
# 5-1. 각 좌표의 숫자마다 BFS를 시작해 연결 덩어리를 찾기
# 5-2. 각 빙산 칸마다 네 방향을 확인해 바다의 수 계산 후 칸의 숫자 업데이트
# 5-2-1. 단, 음수가 되지 않도록 max(..., 0) 함수 사용
# 5-3. 빙산이 2개 이상이면 시간 출력 후 종료
# 5-4. 빙산이 모두 녹았다면 0을 출력 후 종료
# 5-4. 시간을 1 증가

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def count_components():
    visited = [[False] * M for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(M):
            if grid[i][j] and not visited[i][j]:
                bfs(i, j, visited)
                cnt += 1

    return cnt


def bfs(x, y, visited):
    q = deque()
    q.append([x, y])
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and grid[nx][ny] > 0:
                    visited[nx][ny] = True
                    q.append([nx, ny])


def melt():
    melt_list = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if grid[i][j]:
                sea = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < N and 0 <= ny < M:
                        if grid[nx][ny] == 0:
                            sea += 1
                melt_list[i][j] = sea

    for i in range(N):
        for j in range(M):
            if grid[i][j]:
                grid[i][j] = max(grid[i][j] - melt_list[i][j], 0)


time = 0
while True:
    components = count_components()

    if components >= 2:
        print(time)
        break

    if not components:
        print(0)
        break

    melt()
    time += 1
