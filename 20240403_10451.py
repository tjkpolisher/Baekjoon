# 10451: 순열 사이클
# 알고리즘 분류: 그래프 이론/그래프 탐색/순열 사이클 분할

# 1. 테스트 케이스의 수 T 입력
# 2. [반복문]
# 2-1. 순열의 크기 N 입력
# 2-2. 순열 입력
# 2-3. 1번부터 N번까지 순열의 각 원소가 연결되어 있는 다른 노드와 연결한 그래프 생성
# 2-3 보충설명: 단방향 간선입니다.
# 2-4. 노드를 DFS로 순회하면서 방문 처리 된 노드를 다시 방문하면 순환 판정.
# 2-5. 순열 사이클의 개수 출력

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(graph, node, visited):
    visited[node] = True
    next_node = graph[node][0]
    if not visited[next_node]:
        dfs(graph, next_node, visited)


T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    sequence = list(map(int, input().split()))
    graph = [[] for _ in range(N + 1)]
    for i, n in enumerate(sequence):
        graph[i + 1].append(n)

    visited = [False] * (N + 1)
    cnt = 0
    for i in range(1, N + 1):
        if not visited[i]:
            dfs(graph, i, visited)
            cnt += 1
    print(cnt)
