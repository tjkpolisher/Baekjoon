# 9372: 상근이의 여행
# 특이사항: 다국어(영어)(한국어 번역)
# 알고리즘 분류: 그래프 이론/트리

# 1. 테스트 케이스의 수 T 입력
# 2. [반복문]
# 2-1. 국가의 수 (2 ≤ N ≤ 1,000)과 비행기의 종류 M(1 ≤ M ≤ 10,000) 입력
# 2-2. M개의 줄에 걸쳐 a와 b의 쌍 입력(a와 b를 "왕복"함을 의미)
# 2-3. BFS를 이용해 최소 경로를 구하면 비행기 종류의 최소 개수를 구할 수 있음
# 2-4. 최소 개수 출력

import sys
from collections import deque
input = sys.stdin.readline


def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True
    ans = 0
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                ans += 1
    return ans


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    graph = [[] for i in range(N + 1)]
    visited = [False] * (N + 1)
    for i in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    print(bfs(graph, 1, visited))


# 스포일러: 사실 이 문제는 모든 나라가 연결 그래프를 이루고 있다는 점 때문에 N-1로 답이 정해져있습니다...
