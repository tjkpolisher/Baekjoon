# 17204: 죽음의 게임
# 출처: 중앙대학교 2019 NPC (Newbie Programming Contest) D번
# 알고리즘 분류: 구현/그래프 이론/그래프 탐색/시뮬레이션

# 1. 게임에 참여하는 사람의 수 N, 보성이의 번호 K 입력 (3 ≤ N ≤ 150, 1 ≤ K ≤ N - 1)
# 2. N줄에 걸쳐  i(0 ≤ i ≤ N - 1)번 사람이 지목하는 사람의 번호 a_i(0 ≤ a_i ≤ N - 1) 입력
# [보충설명] 자기 자신을 지목할 수도 있음
# 3. 입력받은 번호에 따라 그래프 구성
# 4. 0번 노드부터 시작해 BFS를 실행하면서 한 번 실행할 때마다 M에 1을 더함
# 5-1. 탐색 결과 가장 작은 양의 정수 M 출력
# 5-2. 어떤 방법으로도 보성이가 걸리지 않으면 -1을 출력

from collections import deque

N, K = map(int, input().split())
graph = [[] for _ in range(N)]
for i in range(N):
    graph[i].append(int(input()))


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    count = 0

    while queue:
        v = queue.popleft()
        if v == K:
            return count
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
        count += 1

    return -1


visited = [False] * N
print(bfs(graph, 0, visited))
