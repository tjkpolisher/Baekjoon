# 25418: 정수 a를 k로 만들기
# 알고리즘 분류: 다이나믹 프로그래밍/그래프 이론/그래프 탐색/너비 우선 탐색

# 1. 양의 정수 A와 K 입력 (1 ≤ A < K ≤ 1,000,000)
# 2. A와 K까지의 수에 대하여 x + 1, x * 2를 저장한 그래프 생성
# 3. 그래프에 대하여 BFS를 실행해 연산 횟수 측정
# 4. K를 나타내는 노드에 도착하면 연산 횟수 출력

from collections import deque

A, K = map(int, input().split())

graph = [[] for _ in range(K + 1)]
for i in range(A, K + 1):
    tmp1 = i + 1
    tmp2 = i * 2

    # 계산한 값들이 K 이하일 때만 그래프에 append
    if tmp1 <= K:
        graph[i].append(tmp1)
    if tmp2 <= K:
        graph[i].append(tmp2)

visited = [False for _ in range(K + 1)]


def bfs(start):
    # 큐 초기화 및 시작 노드(A번 노드) 방문 처리
    q = deque()
    visited[start] = True
    for node in graph[start]:
        q.append(node)
    cnt = 0  # 연산 횟수
    while q:
        for _ in range(len(q)):
            x = q.popleft()
            visited[x] = True
            for j in graph[x]:
                if not visited[j]:
                    q.append(j)
        cnt += 1
        if visited[K]:
            return cnt


print(bfs(A))
