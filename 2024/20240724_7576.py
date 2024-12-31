# 7576: 토마토
# 출처: 한국정보올림피아드 지역본선 2013 고등부 1번
# 알고리즘 분류: 그래프 이론/그래프 탐색/너비 우선 탐색

# 1. 상자의 가로 칸, 세로 칸을 나타내는 정수 M, N 입력 (2 ≤ M,N ≤ 1,000)
# 2. N개의 줄에 걸쳐 토마토의 정보 입력
# 2-1. 정보 입력 시 익은 토마토의 최초 위치 인덱스를 포착해 기록
# 3. 각 토마토의 위치로부터 BFS를 실시해, 가능한 모든 토마토가 익을 때까지의 반복문 실행 횟수를 저장
# 4-1. 만약 익지 않은 토마토가 있을 경우, -1 출력
# 4-2. 다 익었을 경우, 반복문 횟수 출력

from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
tomato_box = []
ripen = []
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(M):
        if line[j] == 1:
            ripen.append((j, i))
    tomato_box.append(line)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(ripen):
    q = deque(ripen)
    cnt = -1
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < M and 0 <= ny < N and tomato_box[ny][nx] == 0:
                    tomato_box[ny][nx] = 1
                    q.append((nx, ny))
        cnt += 1
    return cnt


cnt = bfs(ripen)
for i in range(N):
    for j in range(M):
        if tomato_box[i][j] == 0:
            cnt = -1
print(cnt)
