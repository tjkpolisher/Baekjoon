# 14940: 쉬운 최단거리
# 출처: 2017 서강대학교 Programming Contest Master F번
# 알고리즘 분류: 그래프 이론/그래프 탐색/너비 우선 탐색

# 1. 지도의 세로/가로 크기 n, m 입력 (2 ≤ n ≤ 1000, 2 ≤ m ≤ 1000)
# 2. n개의 줄에 걸쳐 m개의 숫자 입력
# [보충설명] 0은 갈 수 없는 땅, 1은 갈 수 있는 땅, 2는 목표 지점
# [보충설명] 입력에서 2는 단 한 개 주어짐.
# 3. 2인 칸에서 출발해 각 칸으로 도달하는 거리를 계산하기 위해 BFS 실시
# 3-1. n * m 크기의 2차원 배열 생성(각 원소를 -1로 초기화)
# 3-2. 순회 중 현재 칸의 번호가 2 또는 0이면 0으로 변환
# 3-3. 나머지 칸은 목표 지점까지의 최단 거리로 변환
# 3-4. 원래 갈 수 있는 땅 중 목표 위치에 도달할 수 없는 위치는 -1로 남음
# 4. BFS 처리 후 닿을 수 없는 곳에 있는 갈 수 없는 땅을 0으로 변환
# 5. 연산이 끝난 지도를 출력

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
map_array = []
for i in range(n):
    line = list(map(int, input().split()))
    if 2 in line:
        y = i
        x = line.index(2)
    map_array.append(line)

# print(f"{x=}, {y=}")
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
map2 = [[-1] * m for _ in range(n)]
map2[y][x] = 0


def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or ny >= n or nx >= m:
                continue
            if map_array[ny][nx] == 0:
                map2[ny][nx] = 0
            if map_array[ny][nx] == 1 and map2[ny][nx] == -1:
                map2[ny][nx] = map2[y][x] + 1
                q.append((nx, ny))


bfs(x, y)
for i in range(n):
    for j in range(m):
        if map_array[i][j] == 0:
            map2[i][j] = 0

for i in range(n):
    print(*map2[i])
