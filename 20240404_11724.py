# 11724: 연결 요소의 개수
# 알고리즘 분류: 그래프 이론/그래프 탐색/너비 우선 탐색/깊이 우선 탐색

# 1. 노드 개수 N, 간선 개수 M 입력(1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2)
# 2. M개의 줄에 걸쳐 간선의 양 끝점 u와 v 입력(간선 중복 없음)
# 3. 간선의 방향이 없으므로 그래프의 u에서 v로 가는 방향과 v에서 u로 가는 방향 동시 입력
# 4. DFS를 실시하면서 연결 요소, 즉 사이클이 만들어지는 개수 카운팅
# 5. 연결 요소의 개수 출력

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N + 1)


def dfs(graph, node, visited):
    visited[node] = True
    for next in graph[node]:
        if not visited[next]:
            dfs(graph, next, visited)


cnt = 0
for i in range(1, N + 1):
    if not visited[i]:
        dfs(graph, i, visited)
        cnt += 1

print(cnt)
