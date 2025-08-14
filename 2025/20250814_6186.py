# 6186: Best Grass
# 특이사항: 다국어(영어)
# 출처: USACO US Open 2008 Bronze 1번
# 알고리즘 분류: 구현/그래프 이론/그래프 탐색/너비 우선 탐색

# 1. 격자의 행의 개수 R, 열의 개수 C 입력 (1 ≤ R,C ≤ 100)
# 2. R개의 줄에 걸쳐 #(풀) 또는 .(빈 땅)을 포함하는 문자열 입력(각 줄의 길이는 C)
# 3. 풀의 위치를 기록
# 4. 풀의 위치를 순회하면서 BFS를 통해 상하좌우에 인접한 다른 풀이 있는지 확인
# 5. 이동이 불가능하면 카운터에 1을 더함
# 6. 모든 풀을 순회한 후 카운터 출력

import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
grid = []
crump = []
for i in range(R):
    line = list(input().rstrip())
    for j in range(C):
        if line[j] == '#':
            crump.append((i, j))
    grid.append(line)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
visited = set()


def bfs(a, b):
    global cnt
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        visited.add((x, y))
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if grid[nx][ny] == '#' and (nx, ny) not in visited:
                    q.append((nx, ny))
    cnt += 1


for c in crump:
    a, b = c
    if (a, b) not in visited:
        bfs(a, b)

print(cnt)
