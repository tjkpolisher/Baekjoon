# 10971: 외판원 순회 2
# 알고리즘 분류: 브루트포스 알고리즘/백트래킹/외판원 순회 문제

# 1. 도시의 수 N 입력 (2 ≤ N ≤ 10)
# 2. N개의 줄에 걸쳐 비용 행렬 입력(0 ≤ 비용 ≤ 1,000,000)
# 3. DFS를 실행하면서 depth = N - 1이 되면 종료
# 3-1. 도시를 방문할 때마다 경로 비용을 더하고 함수를 재귀적으로 호출
# 3-2. depth = N - 1이 되었을 때 비용 총합이 최소값보다 작으면 정답 갱신
# 4. 정답 출력

import sys
input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

cost = 0
visited = [False] * N
ans = 10 ** 9


def dfs(depth, node):
    global ans, cost
    if depth == N - 1:
        if graph[node][0]:
            cost += graph[node][0]
            if cost < ans:
                ans = cost
            cost -= graph[node][0]
        return

    for i in range(1, N):
        if not visited[i] and graph[node][i]:
            visited[i] = True
            cost += graph[node][i]
            dfs(depth + 1, i)
            visited[i] = False
            cost -= graph[node][i]


dfs(0, 0)
print(ans)
