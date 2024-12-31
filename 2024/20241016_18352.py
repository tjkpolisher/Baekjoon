# 18352: 특정 거리의 도시 찾기
# 알고리즘 분류: 그래프 이론/그래프 탐색/너비 우선 탐색/최단 경로/데이크스트라

# 1. 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시 번호 X 입력
# [보충설명] 2 ≤ N ≤ 300,000, 1 ≤ M ≤ 1,000,000, 1 ≤ K ≤ 300,000, 1 ≤ X ≤ N
# 2. M개의 줄에 걸쳐서 두 자연수 A, B가 공백으로 구분되어 입력(1 ≤ A,B ≤ N)
# 3. A에서 B로 가는 단방향 도로를 나타내는 그래프 생성
# 4. BFS를 실행해 최단 거리가 K인 도시의 번호를 저장
# 5. 저장된 도시의 번호를 오름차순으로 출력하되, 하나도 없을 경우 -1을 출력

import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]  # 도시와 도로 정보를 담은 그래프
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)


def bfs(start, K):
    q = deque()
    q.append(start)
    visited = {i: False for i in range(N + 1)}
    visited[start] = True
    cnt = 0
    answer = []
    while q:
        if cnt == K:
            while q:
                answer.append(q.popleft())
            return answer
        for _ in range(len(q)):
            v = q.popleft()
            if graph[v]:
                for i in graph[v]:
                    if not visited[i]:
                        q.append(i)
                        visited[i] = True
            else:
                if not visited[i]:
                    visited[i] = True
        cnt += 1


answer = bfs(X, K)
if not answer:
    # 최단 거리가 K인 도시가 하나도 존재하지 않을 경우
    print(-1)
else:
    answer.sort()  # 오름차순 정렬
    for a in answer:
        print(a)
