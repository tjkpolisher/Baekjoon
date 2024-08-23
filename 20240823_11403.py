# 11403: 경로 찾기
# 알고리즘 분류: 그래프 이론/그래프 탐색/최단 경로/플로이드-워셜

# 1. 정점의 개수 N 입력 (1 ≤ N ≤ 100)
# 2. 플로이드 워셜 알고리즘을 수행하기 위해 그래프의 인접 행렬 요소를 모두 무한대로 초기화
# 3. 자기 자신을 향하는 비용은 0으로 초기화
# 4. N개의 줄에 걸쳐 그래프의 인접 행렬 정보를 입력
# 5. BFS를 실행하여 각 정점이 연결되어 있다면 check에 1을 기록
# 6. 동시에 각 정점을 방문하면서 visited 배열을 기록
# 7. visited의 결과를 인접 행렬 형식으로 출력

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))
visited = [[0] * N for _ in range(N)]


def bfs(start):
    q = deque()
    q.append(start)
    check = [0 for _ in range(N)]

    while q:
        v = q.popleft()
        for i in range(N):
            if not check[i] and graph[v][i]:
                q.append(i)
                check[i] = 1
                visited[start][i] = 1


for i in range(N):
    bfs(i)

for i in visited:
    print(*i)
