# 1260: DFS와 BFS
# 알고리즘 분류: 그래프 이론/그래프 탐색/너비 우선 탐색/깊이 우선 탐색

# 1. 정점의 개수 N 입력, 간선의 개수 M, 시작 노드 V 입력
# 2. M개의 줄에 걸쳐 간선이 연결하는 두 정점의 번호 입력(양방향 간선)
# 2-1. 그래프를 구성하는 각 노드에 대하여 연결된 다른 노드의 번호를 append
# 3. DFS를 수행한 결과를 먼저 한 줄로 출력
# 4. BFS를 수행한 결과를 한 줄로 출력

from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 2)]
for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for i in range(1, N + 2):
    graph[i] = sorted(graph[i])


def dfs(graph, start, visited):
    v = start
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    visited[start] = True
    queue = deque([start])
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


visited = [False] * (N + 1)
dfs(graph, V, visited)
print()

visited = [False] * (N + 1)
bfs(graph, V, visited)
