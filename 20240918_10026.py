# 10026: 적록색약
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: USA Computing Olympiad March 2014 Contest Bronze 3번
# 알고리즘 분류: 그래프 이론/그래프 탐색/너비 우선 탐색/깊이 우선 탐색

# 1. 그리드의 칸 수 N 입력 (1 ≤ N ≤ 100)
# 2. N개의 줄에 걸쳐 그림을 나타내는 문자열 입력
# 3. 색약이 없을 때를 기준으로 BFS를 실행해 구역의 개수 세기
# 4. 색약이 있을 때를 기준으로 BFS를 실행해 구역의 개수 세기
# [보충설명] 적록색약은 빨간색(R)과 초록색(G)를 구분하지 못하므로 같은 구역으로 취급
# 5. 두 경우의 구역의 개수를 한 줄에 공백으로 구분해 출력

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
grid = []
for _ in range(N):
    grid.append(list(input().rstrip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, color, visited, grid):
    q = deque()
    q.append((x, y))
    visited[y][x] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[ny][nx] and grid[ny][nx] == color:
                    visited[ny][nx] = True
                    q.append((nx, ny))


visited_normal = [[False] * N for _ in range(N)]
count_normal = 0
for j in range(N):
    for i in range(N):
        if not visited_normal[j][i]:
            bfs(i, j, grid[j][i], visited_normal, grid)
            count_normal += 1

graph_rg = [row[:] for row in grid]  # 원본 그래프 복사
for j in range(N):
    for i in range(N):
        if graph_rg[j][i] == 'G':
            graph_rg[j][i] = 'R'

visited_rg = [[False] * N for _ in range(N)]
count_rg = 0

for j in range(N):
    for i in range(N):
        if not visited_rg[j][i]:
            bfs(i, j, graph_rg[j][i], visited_rg, graph_rg)
            count_rg += 1

print(count_normal, count_rg)
