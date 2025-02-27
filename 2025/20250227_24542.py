# 24542: 튜터-튜티 관계의 수
# 출처: 2022 신촌지역 대학생 프로그래밍 대회 동아리 연합 겨울 대회 (SUAPC 2022 Winter) A번
# 알고리즘 분류: 자료 구조/그래프 이론/그래프 탐색/분리 집합

# 1. 교육생의 수 N, 친분 관계의 수 M 입력 (2 ≤ N ≤ 200,000, 1 ≤ M ≤ N - 1)
# 2. M개의 줄에 걸쳐 친분 관계를 맺는 두 교육생 u, v 입력(1 ≤ u,v ≤ N, u ≠ v)
# 3. 입력받은 교육생의 관계를 그래프에 입력
# 4. BFS를 실시해 독립된 그래프를 구분
# 4-1. 어떤 노드에서 BFS를 실시했을 때 방문할 수 있는 모든 노드를 방문 처리
# 4-2. 다음 노드에서 BFS를 실시했을 때 방문했다면 그 노드는 실시하지 않고 pass
# 4-3. 방문하지 않은 노드에 대해서만 BFS 실시 후, 그 결과 방문한 노드의 개수를 정답에 곱함
# 5. 정답을 1,000,000,007로 나눈 나머지 출력

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 1
visited = [False] * (N + 1)


def bfs(n):
    counter = 0
    q = deque()
    q.append(n)
    visited[n] = True

    while q:
        x = q.popleft()
        counter += 1

        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

    return counter


for i in range(1, N + 1):
    if not visited[i]:
        cnt *= bfs(i)

print(cnt % 1000000007)
