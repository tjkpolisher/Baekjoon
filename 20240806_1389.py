# 1389: 케빈 베이컨의 6단계 법칙
# 알고리즘 분류: 그래프 이론/그래프 탐색/너비 우선 탐색/최단 경로/플로이드-워셜

# 1. 유저의 수 N (2 ≤ N ≤ 100)과 친구 관계의 수 M (1 ≤ M ≤ 5,000) 입력
# 2. M개의 줄에 걸쳐 친구 관계 입력
# 3. 입력되는 친구 관계에 따라 양방향 그래프를 구성
# 4-1. 1번 노드부터 BFS를 실행해 각 노드에 도달하는 최소 횟수 측정
# 4-2. 모든 노드 순회 시 최소 횟수를 모두 더해서 케빈 베이컨 수 계산
# 4-3. 케빈 베이컨 수가 기존의 값보다 작을 경우 정답을 해당 노드 번호로 갱신(단, 같은 수일 경우 더 작은 수가 정답)
# 5. 정답 출력

from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# print(f"{graph=}")


def bfs(start, N):
    kb_num = [0] * (N + 1)
    cnt = 0
    visited = [False] * (N + 1)
    visited[start] = True
    q = deque(graph[start])

    while q:
        # print(f"{q=}")
        cnt += 1
        length = len(q)
        for _ in range(length):
            v = q.popleft()
            if not visited[v]:
                visited[v] = True
                kb_num[v] = cnt
                for i in range(len(graph[v])):
                    q.append(graph[v][i])
    # print(f"{kb_num=}")
    return sum(kb_num)


ans = 1
cnt = 10 ** 9  # 초기값
for i in range(1, N + 1):
    cnt_tmp = bfs(i, N)
    if cnt_tmp < cnt:
        ans = i
        cnt = cnt_tmp
print(ans)
