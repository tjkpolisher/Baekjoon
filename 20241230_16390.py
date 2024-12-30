# 16390: Sheba's Amoebas
# 특이사항: 다국어(영어)
# 출처: NCNA 2017 G번
# 알고리즘 분류: 그래프 이론/그래프 탐색/너비 우선 탐색/깊이 우선 탐색

# 1. 두 정수 m, n 입력 (1 ≤ m, n ≤ 100)
# 2. m개의 줄에 걸쳐 n개의 문자로 구성된 문자열 입력
# [보충설명] 문자열에서 '#'은 검은 픽셀을, '.'은 하얀 픽셀을 각각 의미
# [보충설명] 모든 검은 픽셀에 대하여, 이웃하고 있는 픽셀들 중 정확히 2개는 검은 픽셀.
# 3. 첫 번째 픽셀부터 BFS를 실행하면서 루프를 구성하고 있는지 확인
# 3-1. 루프 구성이 확인되면 카운터에 1을 더함
# 3-2. 루프가 아닌 하얀 픽셀이면 다음 방문하지 않은 픽셀로 이동
# [보충설명] 인접한 픽셀은 가로, 세로, 대각선까지 총 여덟 방향을 확인해야 함
# 4. 총 루프 수 카운터 출력

import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(m)]


def bfs(x, y):
    q = deque()
    q.append((x, y))

    # 이동 방향
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    dy = [1, 1, 1, 0, 0, -1, -1, -1]

    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '#':
                grid[nx][ny] = '.'
                q.append((nx, ny))


cnt = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == '#':
            bfs(i, j)
            cnt += 1
print(cnt)
