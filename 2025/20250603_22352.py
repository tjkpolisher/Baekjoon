# 22352: 항체 인식
# 출처: UCPC 2021 예선 B번
# 알고리즘 분류: 그래프 이론/그래프 탐색/너비 우선 탐색/깊이 우선 그래프/격자 그래프

# 1. 격자의 크기 N, M 입력 (1 ≤ N,M ≤ 30)
# 2. N개의 줄에 걸쳐 백신 접종 전 촬영 결과 입력
# 3. 다음 N개의 줄에 걸쳐 백신 접종 후 촬영 결과 입력
# 4. 촬영 전과 후가 완전히 동일할 경우 YES 출력 후 종료
# 5. 두 격자에서 첫 번째로 다른 칸을 탐색
# 6. BFS를 실시해 상하좌우로 움직이면서 격자 탐색
# 7. 찾은 좌표들을 new_val로 일괄 업데이트
# 8. 업데이트 후 격자가 post와 동일한 지 확인 후 같으면 YES, 다르면 NO 출력

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

post = []
for _ in range(N):
    post.append(list(map(int, input().split())))

if grid == post:
    print("YES")
    exit()

start_r = start_c = None
for i in range(N):
    for j in range(M):
        if grid[i][j] != post[i][j]:
            start_r, start_c = i, j
            break
    if start_r is not None:
        break

orig_val = grid[start_r][start_c]
new_val = post[start_r][start_c]
orig_grid = [row[:] for row in grid]

visited = [[False] * M for _ in range(N)]
q = deque()
q.append((start_r, start_c))
visited[start_r][start_c] = True
component = [(start_r, start_c)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while q:
    r, c = q.popleft()
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            if orig_grid[nr][nc] == orig_val:
                visited[nr][nc] = True
                q.append((nr, nc))
                component.append((nr, nc))

for r, c in component:
    grid[r][c] = new_val

if grid == post:
    print("YES")
else:
    print("NO")
