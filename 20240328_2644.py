# 2644: 촌수계산
# 알고리즘 분류: 그래프 이론/그래프 탐색/너비 우선 탐색/깊이 우선 탐색

# 1. 사람의 수 n 입력
# 2. 촌수를 계산해야 하는 서로 다른 두 사람의 번호 입력
# 3. 부모 자식들 간의 관계의 개수 m 입력
# 4. [반복문] m줄에 걸쳐 부모 자식간의 관계를 나타내는 두 번호 x, y 입력 후 그래프로 조직
# 5. BFS를 실시해 1번 노드로부터 찾고자 하는 번호까지의 차수 탐색
# 6. 두 차수를 더해서 출력(단, 어느 한 쪽이라도 탐색하지 못하면 -1을 출력)

from collections import deque


def bfs(start, result, visited):
    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()

        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                result[i] = result[v] + 1
                visited[i] = True


n = int(input())
a1, a2 = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

result = [0] * (n + 1)
visited = [False] * (n + 1)
bfs(a1, result, visited)
print(result[a2] if result[a2] > 0 else -1)
