# 2178: 미로 탐색
# 알고리즘 분류: 그래프 이론/그래프 탐색/너비 우선 탐색

# 1. 미로의 가로와 세로 크기 N, M 입력 (2 ≤ N, M ≤ 100)
# 2. N개의 줄에 걸쳐 M개의 정수로 미로 입력
# [보충설명] 각각의 수들은 '붙어서' 입력으로 주어짐. 1은 이동 가능 칸/0은 이동할 수 없는 칸
# 3. (1, 1)(인덱스 상으로는 (0, 0))에서 출발해 (N, M)의 위치로 이동할 때 지나야 할 최소 칸 수를 BFS로 측정

import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
maze = []
for _ in range(N):
    maze_line = list(input().rstrip())
    maze.append(maze_line)


def bfs(start):
    q = deque()
    q.append(start)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 1
    while q:
        cnt += 1
        length = len(q)
        for _ in range(length):
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= M or ny < 0 or ny >= N:
                    continue
                if maze[ny][nx] == '0':
                    continue
                if maze[ny][nx] == '1':
                    q.append((nx, ny))
                    maze[ny][nx] = 0
                if ny == N - 1 and nx == M - 1:
                    return cnt
    return cnt


print(bfs((0, 0)))
