# 3182: 한동이는 공부가 하기 싫어!
# 특이사항: 다국어(영어)(한국어 번역)
# 알고리즘 분류: 그래프 이론/브루트포스 알고리즘/그래프 탐색

# 1. 정수 N 입력
# 2. N개 줄에 걸쳐 선배들의 대답 입력 후 그래프로 구성
# 3. dfs를 실행해 가장 노드 깊이가 각 노드의 최대 탐색 깊이를 리스트에 입력
# 4. 노드 번호와 깊이를 저장한 리스트를 깊이 기준으로 내림차순으로 정렬
# 5. 한동이가 물어봐야 할 선배의 번호의 최소값 출력


def dfs(graph, node, visited):
    global cnt
    visited[node] = True
    v = graph[node][0]
    if not visited[v]:
        cnt += 1
        dfs(graph, v, visited)
    return cnt


N = int(input())
graph = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    idx = int(input())
    graph[i].append(idx)

counters = []
for i in range(1, N + 1):
    visited = [False] * (N + 1)
    global cnt
    cnt = 0
    cnt = dfs(graph, i, visited)
    counters.append((i, cnt))
counters.sort(key=lambda x: x[1], reverse=True)
print(counters[0][0])
