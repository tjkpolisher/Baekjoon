# 21736: 헌내기는 친구가 필요해
# 출처: 제1회 숙명여자대학교 교내 알고리즘 경진대회 (SMUPC) C번
# 특이사항: 시간 제한(Python 3 2초, PyPy3 2초)
# 알고리즘 분류: 그래프 이론/그래프 탐색/너비 우선 탐색/깊이 우선 탐색

# 1. 캠퍼스의 크기 N, M 입력 (1 ≤ N,M ≤ 600)
# 2. N개의 줄에 걸쳐 캠퍼스의 정보 입력
# [보충설명] O: 빈 공간, X: 벽, I: 도연이, P: 사람, I는 한 번만 주어짐.
# 3. I에서부터 BFS를 실행해 P를 만날 때마다 카운터를 올림
# 4. 도연이가 만날 수 있는 사람의 수를 출력하되, 아무도 만나지 못할 경우 'TT'를 출력

from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y):
    cnt = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue
            if graph[ny][nx] == 'X':
                continue
            if graph[ny][nx] == 'P' or graph[ny][nx] == 'O':
                if graph[ny][nx] == 'P':
                    cnt += 1
                graph[ny][nx] = 'X'
                q.append((nx, ny))
    return cnt


N, M = map(int, input().split())
graph = []
for i in range(N):
    info = input().rstrip()
    if 'I' in info:
        ix = info.index('I')
        iy = i
    graph.append(list(info))

ans = bfs(ix, iy)
if not ans:
    ans = 'TT'
print(ans)
