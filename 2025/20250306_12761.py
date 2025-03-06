# 12761: 돌다리
# 출처: 2016 전북대 프로그래밍 경진대회 G번
# 알고리즘 분류: 그래프 이론/그래프 탐색/너비 우선 탐색

# 1. 스카이 콩콩의 힘 A와 B, 동규와 주미의 현재 위치 N, M 입력
# [보충설명] 2 ≤ A,B ≤ 30, 0 ≤ N,M ≤ 100,000
# 2. BFS를 실시하되, 두 시작 노드로부터 가능한 여덟 개의 경우의 수에 따라 큐에 노드 삽입
# 2-1. 이때, 시작 노드를 포함해 방문한 노드는 방문 처리
# 2-2. M번 노드가 방문 처리되어 있을 경우 루프 종료
# 3. 이동 횟수 출력

from collections import deque

A, B, N, M = map(int, input().split())
cnt = 0  # 이동 횟수


def bfs(N, M):
    global cnt

    visited = [False] * 100001  # 방문 처리 리스트
    visited[N] = True  # 시작 노드는 방문 처리

    q = deque()
    q.append(N)
    d = [1, -1, A, -A, B, -B, A, B]  # 이동 가능한 경우의 수

    while q:
        for _ in range(len(q)):
            x = q.popleft()
            for i in range(8):
                if i < 6:
                    nx = x + d[i]
                else:
                    nx = x * d[i]

                if 0 <= nx <= 100000 and not visited[nx]:
                    visited[nx] = True
                    q.append(nx)

        cnt += 1
        if visited[M]:
            break


bfs(N, M)
print(cnt)
