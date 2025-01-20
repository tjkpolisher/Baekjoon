# 5958: Space Exploration
# 특이사항: 다국어(영어)
# 출처: USACO January 2011 Contest Bronze 3번
# 알고리즘 분류: 그래프 이론/그래프 탐색/너비 우선 탐색/깊이 우선 탐색

# 1. 공간의 한 변의 길이 N 입력 (1 ≤ N ≤ 1000)
# 2. N개의 줄에 걸쳐 공간 및 소행성 정보 입력(소행성은 '*' 문자, 빈 공간은 '.' 문자로 입력됨)
# 3. 입력받은 공간 정보를 순회하면서 소행성이 등장할 때마다 BFS를 실행
# 4. 현재 탐색 중인 소행성 영역을 모두 탐색했으면 카운터에 1을 올림.
# 5. 모두 탐색이 끝나면 카운터를 출력

import sys
input = sys.stdin.readline

N = int(input())
space = [list(input().rstrip()) for _ in range(N)]


def bfs(x, y):
    q = [(x, y)]
    space[x][y] = '.'  # 이미 방문한 영역을 방문 처리(빈 공간으로 취급)
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and space[nx][ny] == '*':
                space[nx][ny] = '.'
                q.append((nx, ny))


cnt = 0
for j in range(N):
    for k in range(N):
        if space[j][k] == '*':
            bfs(j, k)
            cnt += 1

print(cnt)
