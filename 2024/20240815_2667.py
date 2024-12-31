# 2667: 단지번호붙이기
# 출처: KOI(한국정보올림피아드) 1996 초등부 1번
# 알고리즘 분류: 그래프 이론/그래프 탐색/너비 우선 탐색/깊이 우선 탐색

# 1. 지도의 크기 N (5 ≤ N ≤ 25) 입력
# 2. N개의 줄에 걸쳐 0 또는 1의 숫자들이 N개씩 공백 없이 입력
# 2-1. 1이 입력된 위치의 인덱스를 큐에 입력
# 3. 1이 입력된 위치로부터 BFS를 실행해 가로/세로로만 연결된 단지를 탐색
# 3-1. 더 이상 현재 단지가 연결되지 않을 때까지 BFS를 실행하면서 큐에 숫자 1이 들어갈 때마다 카운터에 1을 더함
# 3-2. 현재 단지에서 BFS가 종료되면 카운터를 단지내 집의 수를 저장하는 리스트에 저장
# 4. 총 단지 수(리스트의 길이) 출력
# 5. 단지 내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
house = []
for i in range(N):
    line_string = input().rstrip()
    line = []
    for j in range(N):
        line.append(int(line_string[j]))
    house.append(line)


def bfs(start):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 1
    q = deque()
    q.append(start)
    y_start, x_start = start[0], start[1]
    house[y_start][x_start] = 0
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if house[ny][nx] == 1:
                q.append((ny, nx))
                house[ny][nx] = 0
                cnt += 1
    return cnt


house_per_groups = []
for i in range(N):
    for j in range(N):
        if house[i][j] == 1:
            house_per_groups.append(bfs((i, j)))

print(len(house_per_groups))
for counts in sorted(house_per_groups):
    print(counts)
