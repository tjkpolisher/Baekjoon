# 7569: 토마토
# 출처: 한국정보올림피아드 지역본선 2013 초등부 3번
# 알고리즘 분류: 그래프 이론/그래프 탐색/너비 우선 탐색

# 1. 상자의 크기를 나타내는 두 정수 M, N, 쌓아올리는 상자의 수 H 입력
# [보충설명] 2 ≤ M ≤ 100, 2 ≤ N ≤ 100, 1 ≤ H ≤ 100
# 2. N개의 줄에 걸쳐 가장 밑의 상자부터 위의 상자까지에 저장된 토마토들의 정보 입력
# 2-1. 각 줄에 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어짐.
# 2-2. 토마토가 위치한 지점의 인덱스는 따로 기록
# [보충설명] 1은 익은 토마토, 0은 익지 않은 토마토, -1은 토마토가 없는 칸
# 3. 3차원 그래프에 대한 BFS를 실행하여 토마토가 존재하는 영역부터 탐색
# 3-1. 탐색 후 익지 않은 토마토가 발견되면, 해당 칸의 숫자를 1로 바꿈.
# 3-2. 한 번의 반복문 실행 중 큐에 있는 모든 원소를 다 꺼낸 경우 카운터에 1을 더함
# 4. 익지 않은 토마토(0)이 남아있는 지 전체 순회
# 4-1. 모두 익었을 경우 카운터의 횟수 출력
# 4-2. 익지 않은 토마토가 발견된 경우 -1을 출력하고 프로그램 종료

import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
graph = []
q = deque()
for i in range(H):
    layer = []
    for j in range(N):
        row = list(map(int, input().rstrip().split()))
        for k in range(M):
            if row[k] == 1:
                q.append((i, j, k))
        layer.append(row)
    graph.append(layer)


def bfs():
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    while q:
        z, y, x = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
                if graph[nz][ny][nx] == 0:
                    graph[nz][ny][nx] = graph[z][y][x] + 1
                    q.append((nz, ny, nx))


bfs()

max_days = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 0:
                print(-1)
                sys.exit(0)
            max_days = max(max_days, graph[i][j][k])
print(max_days - 1)
